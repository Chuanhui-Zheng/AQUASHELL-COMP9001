import os
import random
import select
import shutil
import sys
import termios
import time
import tty
from dataclasses import dataclass

import handbook
from handbook import CYAN, GREEN, MAGENTA, RED, RESET, YELLOW, sprite_height, sprite_lines, sprite_width


@dataclass
class Creature:
    name: str
    kind: str
    sprite: str
    source: str = "unknown"
    capacity: int = 1
    shiny: bool = False
    starts_left: bool = False
    bottom: bool = False
    stationary: bool = False


def hard_clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def clear_screen():
    print("\033[H", end="")


def terminal_size():
    size = shutil.get_terminal_size((100, 36))
    width = max(96, min(size.columns, 150))
    height = max(38, min(size.lines - 4, 52))
    return width, height


def make_swimmer(creature, width, lane_y):
    fish_width = sprite_width({"sprite": creature.sprite})

    if creature.capacity == 1:
        direction = -1
    else:
        direction = -1 if creature.starts_left else random.choice([-1, 1])

    if creature.name == "Dolphin":
        lane_y = random.choice([5, 6, 7])
        vertical_direction = random.choice([-1, 1])
    elif creature.name == "Starfish":
        vertical_direction = random.choice([-1, 1])
    else:
        vertical_direction = 0

    fast_names = {"Manta Ray", "Squid", "Shark", "Whale"}
    rainbow_colors = [RED, YELLOW, GREEN, CYAN, MAGENTA]

    return {
        "creature": creature,
        "x": random.randint(3, max(4, width - fish_width - 4)),
        "y": lane_y,
        "direction": direction,
        "vertical_direction": vertical_direction,
        "vertical_speed": random.choice([7, 8, 9]) if creature.name == "Starfish" else 1,
        "speed": 1 if creature.name in fast_names else random.choice([3, 4, 5]),
        "turn_after": random.randint(35, 95),
        "shiny_offset": random.randint(0, len(rainbow_colors) * 3 - 1) if creature.shiny else 0,
    }


def make_swimmers(creatures, width, height):
    swimmers = []
    lane_y = 6
    bottom_limit = height - 5

    top_zone_names = {"Jellyfish", "Whale"}
    middle_zone_names = {"Paperfish", "Goldfish", "Seahorse"}
    bottom_zone_names = {"Squid", "Shark", "Manta Ray"}

    def pick_zone_y(preferred_min, preferred_max, fish_height):
        overall_min = 5
        overall_max = max(overall_min, height - fish_height - 4)

        preferred_min = max(overall_min, preferred_min)
        preferred_max = min(overall_max, preferred_max)

        if preferred_min > preferred_max:
            return random.randint(overall_min, overall_max)

        spill = max(2, height // 12)
        spill_min = max(overall_min, preferred_min - spill)
        spill_max = min(overall_max, preferred_max + spill)

        if random.random() < 0.8:
            return random.randint(preferred_min, preferred_max)
        return random.randint(spill_min, spill_max)

    ordered_creatures = sorted(
        creatures,
        key=lambda creature: sprite_height({"sprite": creature.sprite}),
        reverse=True,
    )

    for creature in ordered_creatures:
        fish_height = sprite_height({"sprite": creature.sprite})

        top_min = 5
        top_max = max(top_min, height // 3 - fish_height)

        middle_min = height // 3
        middle_max = max(middle_min, height * 2 // 3 - fish_height)

        bottom_min = height * 2 // 3
        bottom_max = max(bottom_min, height - fish_height - 4)

        if creature.bottom:
            y = max(6, height - fish_height - 4)
        elif creature.name in top_zone_names:
            y = pick_zone_y(top_min, top_max, fish_height)
        elif creature.name in middle_zone_names:
            y = pick_zone_y(middle_min, middle_max, fish_height)
        elif creature.name in bottom_zone_names:
            y = pick_zone_y(bottom_min, bottom_max, fish_height)
        elif lane_y + fish_height > bottom_limit:
            lane_y = random.randint(6, max(6, bottom_limit - fish_height))
            y = lane_y
        else:
            y = lane_y

        swimmers.append(make_swimmer(creature, width, y))

        if not creature.bottom:
            lane_y += fish_height + 2

    return swimmers


def draw_text(canvas, x, y, text, color=None):
    if y < 0 or y >= len(canvas):
        return

    invisible_chars = {" ", "⠀", "\t"}

    for offset, char in enumerate(text):
        column = x + offset
        if 0 <= column < len(canvas[y]) and char not in invisible_chars:
            canvas[y][column] = f"{color}{char}{RESET}" if color else char


def mirror_braille_char(char):
    code = ord(char)

    if 0x2800 <= code <= 0x28FF:
        pattern = code - 0x2800

        dot_pairs = [
            (0, 3),
            (1, 4),
            (2, 5),
            (6, 7),
        ]

        mirrored_pattern = pattern

        for left, right in dot_pairs:
            left_bit = (pattern >> left) & 1
            right_bit = (pattern >> right) & 1

            if left_bit != right_bit:
                mirrored_pattern ^= 1 << left
                mirrored_pattern ^= 1 << right

        return chr(0x2800 + mirrored_pattern)

    return char


def mirror_sprite(sprite):
    lines = str(sprite).splitlines()
    width = max((len(line) for line in lines), default=0)

    mirror_map = str.maketrans({
        "(": ")",
        ")": "(",
        "[": "]",
        "]": "[",
        "{": "}",
        "}": "{",
        "<": ">",
        ">": "<",
        "/": "\\",
        "\\": "/",
    })

    mirrored_lines = []

    for line in lines:
        padded = line.ljust(width)

        mirrored_line = "".join(
            mirror_braille_char(char.translate(mirror_map))
            for char in padded
        )[::-1]

        mirrored_lines.append(mirrored_line)

    return "\n".join(mirrored_lines)


def oriented_sprite(creature, direction):
    if direction < 0:
        return creature.sprite if creature.starts_left else mirror_sprite(creature.sprite)

    return mirror_sprite(creature.sprite) if creature.starts_left else creature.sprite


def draw_sprite(canvas, x, y, creature, direction, color=None):
    sprite = oriented_sprite(creature, direction)
    lines = str(sprite).splitlines()

    for row, line in enumerate(lines):
        draw_text(canvas, x, y + row, line, color)


def update_swimmer(swimmer, width, height, frame_number):
    creature = swimmer["creature"]
    fish_width = sprite_width({"sprite": creature.sprite})
    fish_height = sprite_height({"sprite": creature.sprite})

    if creature.stationary and creature.name != "Starfish":
        return

    if creature.name == "Starfish":
        if frame_number % (swimmer["speed"] * swimmer.get("vertical_speed", 1)) == 0:
            bottom_limit = max(5, height - fish_height - 2)
            top_limit = max(5, bottom_limit - 4)

            swimmer["y"] += swimmer.get("vertical_direction", 1)

            if swimmer["y"] <= top_limit:
                swimmer["y"] = top_limit
                swimmer["vertical_direction"] = 1
            elif swimmer["y"] >= bottom_limit:
                swimmer["y"] = bottom_limit
                swimmer["vertical_direction"] = -1

        return

    if creature.capacity > 1:
        if frame_number % swimmer["turn_after"] == 0 and frame_number != 0:
            swimmer["direction"] *= -1
            swimmer["turn_after"] = random.randint(35, 95)

    if frame_number % swimmer["speed"] == 0:
        swimmer["x"] += swimmer["direction"]

        if creature.name == "Dolphin":
            swimmer["y"] += swimmer.get("vertical_direction", 1)

            if swimmer["y"] <= 5:
                swimmer["y"] = 5
                swimmer["vertical_direction"] = 1
            elif swimmer["y"] >= 9:
                swimmer["y"] = 9
                swimmer["vertical_direction"] = -1

    if creature.capacity == 1:
        if swimmer["x"] + fish_width < 1:
            swimmer["x"] = width - fish_width - 2
    else:
        edge_margin = 3

        if swimmer["x"] <= edge_margin:
            swimmer["x"] = edge_margin
            swimmer["direction"] = 1
        elif swimmer["x"] + fish_width >= width - edge_margin:
            swimmer["x"] = width - fish_width - edge_margin
            swimmer["direction"] = -1


def aquarium_frame(data, swimmers, frame_number):
    width, height = terminal_size()
    waterline = 4
    canvas = [[" " for _ in range(width)] for _ in range(height)]
    rainbow_colors = [RED, YELLOW, GREEN, CYAN, MAGENTA]

    for x in range(width):
        canvas[0][x] = "="
        canvas[height - 1][x] = "="
        canvas[waterline][x] = "~" if x % 2 == frame_number % 2 else "-"

    for y in range(height):
        canvas[y][0] = "|"
        canvas[y][width - 1] = "|"

    draw_text(canvas, 3, 1, "AQUASHELL LIVE TANK", CYAN)
    draw_text(canvas, 3, 2, "Press Enter to return", YELLOW)
    draw_text(canvas, width - 24, 2, f"Coins: {data['coins']}", CYAN)

    for swimmer in sorted(swimmers, key=lambda item: item["creature"].capacity, reverse=True):
        update_swimmer(swimmer, width, height, frame_number)

        creature = swimmer["creature"]
        color = None

        if creature.shiny:
            offset = swimmer.get("shiny_offset", 0)
            color = rainbow_colors[((frame_number + offset) // 3) % len(rainbow_colors)]

        draw_sprite(
            canvas,
            swimmer["x"],
            swimmer["y"],
            creature,
            swimmer["direction"],
            color
        )

    bubbles = [
        (width // 5, height - 7),
        (width // 3, height - 11),
        (width // 2, height - 8),
        (width - width // 4, height - 12),
    ]

    for x, y in bubbles:
        bubble_y = waterline + 2 + ((y - frame_number) % (height - waterline - 8))
        draw_text(canvas, x, bubble_y, "o", CYAN)
        draw_text(canvas, x + 2, bubble_y - 2, ".", CYAN)

    for x in range(3, width - 3, 12):
        draw_text(canvas, x, height - 4, "^^^", CYAN)
        if (x + frame_number) % 3 == 0:
            draw_text(canvas, x + 1, height - 5, "^", CYAN)

    used = handbook.capacity_used(data)
    limit = handbook.capacity_limit(data)
    draw_text(canvas, 3, height - 2, f"Capacity: {used}/{limit}", YELLOW)

    return "\n".join("".join(row) for row in canvas)


class RawTerminal:
    def __enter__(self):
        self.fd = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(self.fd)
        tty.setcbreak(self.fd)
        return self

    def __exit__(self, exc_type, exc, traceback):
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)


def key_pressed():
    ready, _, _ = select.select([sys.stdin], [], [], 0)
    if ready:
        return sys.stdin.read(1)
    return ""


def color(text, value):
    return f"{value}{text}{RESET}"


RELEASE_ART = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣀⣤⣤⣤⣤⣀⠀⠀⠀⣷⡀⠀⠀⢀⣴⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⢿⣿⣿⣿⣿⣿⣿⣴⡶⣿⡷⢶⣦⣾⣿⠁⠀⠀⢀⣤⡾⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠛⠛⣿⣿⣿⣿⠀⠸⠇⠀⣼⡿⠻⣦⣤⣴⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⡟⠀⠀⠀⠀⠛⠀⢀⣼⣿⣿⡁⠀⠀⣀⣠⡤⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⠟⠀⠀⠀⠀⠀⠀⢠⠟⠋⠀⢈⣿⣶⣿⠿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠿⢻⣇⠀⠀⣀⣀⣀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠋⠉⠀⢀⣠⣿⣾⣿⣿⣿⣿⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⠃⠀⠀⢸⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣏⠙⢿⣿⣧⣄⣀⣼⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢷⣤⡈⠛⠿⣿⣿⣿⠇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣷⣦⣄⡉⠛⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠃⠀⠀
"""


def collection_items(data):
    items = []
    names = sorted({handbook.normalize_entry(item)["name"] for item in data.get("inventory", [])})

    for name in names:
        creature = handbook.get_creature(name)
        if not creature:
            continue

        quantity = handbook.count_owned(data, name)
        if quantity <= 0:
            continue

        display = creature.copy()
        display["sprite"] = display.get("tank_sprite", display["sprite"])
        items.append((name, quantity, display))

    return items


def print_collection_items(items):
    by_kind = {}

    for index, (name, quantity, item) in enumerate(items, start=1):
        by_kind.setdefault(item["kind"], []).append((index, name, quantity, item))

    for kind, entries in sorted(by_kind.items()):
        print(f"\n{color(kind.title(), CYAN)}:")
        for index, name, quantity, item in entries:
            print(f"\n  {index}. {name} [{quantity}] | Capacity {item.get('capacity', 1)}")
            for line in sprite_lines(item):
                print(f"     {line}")


def parse_release_command(command, items):
    parts = command.split()

    if len(parts) != 3 or parts[0].lower() != "release":
        return None, None, None

    if not parts[1].isdigit() or not parts[2].isdigit():
        return None, None, None

    index = int(parts[1])
    quantity = int(parts[2])

    if not 1 <= index <= len(items):
        return None, None, None

    name, owned, item = items[index - 1]

    if quantity <= 0 or quantity > owned:
        return None, None, None

    return name, quantity, item


def release_creature(data, command, items, pause):
    name, quantity, item = parse_release_command(command, items)

    if not name:
        pause("Use: release number quantity. Press Enter...")
        return

    removed = handbook.remove_creatures(data, name, quantity, allow_shiny=True)

    hard_clear_screen()
    print(RELEASE_ART)
    print()
    print(f"The fish release failed. {removed} {name} was already cooked and ended up in my belly.")
    pause()


def show_collection(data, pause):
    while True:
        hard_clear_screen()
        print(color("Your Collection", CYAN))
        print("=" * 40)

        items = collection_items(data)

        if not items:
            print("\nYour aquarium is empty.")
            pause()
            return

        print_collection_items(items)
        print()
        print("Type: release number quantity    Example: release 2 1")
        print("Press Enter to return.")

        command = input("\nCollection command: ").strip()

        if command == "":
            return

        if command.lower().startswith("release "):
            release_creature(data, command, items, pause)
        else:
            pause("Unknown collection command. Press Enter...")


def build_creatures(data):
    return [
        Creature(
            item["name"],
            item["kind"],
            item["sprite"],
            item.get("source", "unknown"),
            item.get("capacity", 1),
            item.get("shiny", False),
            item.get("starts_left", False),
            item.get("bottom", False),
            item.get("stationary", False),
        )
        for item in handbook.get_owned_creatures(data)
        if item["kind"] in {"fish", "pet"}
    ]


def run_aquarium(data, swimmers):
    print("\033[2J\033[H", end="")

    with RawTerminal():
        frame_number = 0

        while True:
            print("\033[H", end="")
            print(aquarium_frame(data, swimmers, frame_number))
            print("\nPress C for collection. Press Enter to return.")

            key = key_pressed()

            if key in {"\n", "\r"}:
                return "return"

            if key.lower() == "c":
                return "collection"

            frame_number += 1
            time.sleep(0.12)


def visit_aquarium(data, pause):
    creatures = [*build_creatures(data)]
    width, height = terminal_size()
    swimmers = make_swimmers(creatures, width, height)

    data["visits"] += 1

    try:
        while True:
            action = run_aquarium(data, swimmers)

            if action == "return":
                break

            show_collection(data, pause)

            creatures = build_creatures(data)
            width, height = terminal_size()
            swimmers = make_swimmers(creatures, width, height)

    except (termios.error, OSError):
        for frame_number in range(80):
            print("\033[H", end="")
            print(aquarium_frame(data, swimmers, frame_number))
            time.sleep(0.12)

        pause("Animation preview ended. Press Enter...")