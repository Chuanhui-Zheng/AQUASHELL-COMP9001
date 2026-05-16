import os
import random
import select
import sys
import termios
import time
import tty

import handbook
from handbook import BIG_FISH, FISHING_CATCHES


FISHING_SCENE = r'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⢴⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡿⠟⠋⢁⣼⣷⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡾⠛⠁⣀⣤⡾⠛⠁⢹⣇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠏⢹⡶⠶⠟⠋⠁⠀⠀⠀⠈⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠁⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢾⣟⣁⣤⡾⠋⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠗⠀⣿⠋⠁⠀⠀⠀⠀⠀⠀⣠⣶⠟⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠠⡾⠋⠀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⠘⠢⠀⢀⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡼⠛⠉⠀⠰⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡄⠀⠀⠀
⠀⠀⠀⣰⣿⠁⢼⣿⣷⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⢠⡄⠀⠀⠀
⠀⢠⣾⡿⠋⠀⠈⠉⠁⢠⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸⡇⠀⠀⠀
⠀⠙⠛⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠾⠛⠀⠀⠀⠀
'''


LAKE_SCENE = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⣤⡶⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⡾⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⠏⠀⠀⠀⠀⠀⠀⣠⣶⣿⡿⣷⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⡀⠀⠀⠀⠀⠀⢰⣿⡟⠁⠀⠀⢹⣿⣇⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⣷⣄⠀⠀⠀⠀⠈⣁⣄⠀⠀⠀⣸⣿⡏⠀⠀⠀⠀⠀⠈⣿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠙⠻⠷⠶⠿⠛⠋⢡⣴⣶⣾⣿⣟⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⣿⣿⣧⠀⠀⠀⠀⠀⠀⢸⣿⢿⣿⣆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣷⡀⠀⠀⠀⠀⠘⠁⠀⢻⣿⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣷⡀⠀⠀⠀⠀⠀⠀⣸⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣄⡀⠀⠀⢀⣴⣿⣿⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠉⠁⠀⠀⠀⠀
"""


ROD_RULES = {
    1: {"name": "Basic Rod", "coins": (3, 5), "big_chance": 0.15},
    2: {"name": "Copper Rod", "coins": (5, 8), "big_chance": 0.15},
    3: {"name": "Silver Rod", "coins": (8, 14), "big_chance": 0.15},
    4: {"name": "Golden Rod", "coins": (14, 24), "big_chance": 0.15},
    5: {"name": "Mythic Rod", "coins": (24, 40), "big_chance": 0.15},
}

SMALL_CHANCE = 0.35
BIG_CHANCE = 0.15
COIN_CHANCE = 0.50


class RawTerminal:
    def __enter__(self):
        self.fd = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(self.fd)
        tty.setcbreak(self.fd)
        return self

    def __exit__(self, exc_type, exc, traceback):
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def key_pressed():
    ready, _, _ = select.select([sys.stdin], [], [], 0)
    if ready:
        return sys.stdin.read(1)
    return ""


def show_fishing_scene():
    clear_screen()
    print(FISHING_SCENE)
    print("\nThe island is quiet. Your line sinks into the water...")
    time.sleep(3)


def render_pointer_bar(position, width=31):
    center = width // 2

    cells = ["-" for _ in range(width)]

    left_box = center - 1
    right_box = center

    cells[left_box] = "□"
    cells[right_box] = "□"

    if position == left_box or position == right_box:
        cells[position] = "■"
    else:
        cells[position] = "^"

    return "[" + "".join(cells) + "]"

def timing_challenge():
    if not sys.stdin.isatty():
        input("Press Enter to pull the fishing line...")
        return random.random() < 0.55

    width = 31
    center = width // 2
    position = 0
    direction = 1

    with RawTerminal():
        while True:
            clear_screen()
            print(LAKE_SCENE)
            print("Press SPACE when the pointer is exactly inside the center box.\n")
            print(render_pointer_bar(position, width))
            print(" " * (position + 1) + "|")

            if key_pressed() == " ":
                return position == center or position == center - 1

            position += direction
            if position == 0 or position == width - 1:
                direction *= -1
            time.sleep(0.045)


def render_fight_bar(progress):
    width = 30
    filled = int(width * progress / 100)
    return "[" + "#" * filled + "-" * (width - filled) + f"] {progress:>3}%"


def big_fish_fight():
    if not sys.stdin.isatty():
        input("Press Enter to fight the big fish...")
        return random.random() < 0.45

    progress = 35
    last_decay = time.time()

    with RawTerminal():
        while 0 < progress < 100:
            clear_screen()
            print(LAKE_SCENE)
            print("A heavy fish is fighting back!")
            print("Keep pressing SPACE until the bar is full.\n")
            print(render_fight_bar(progress))

            if key_pressed() == " ":
                progress = min(100, progress + 8)

            now = time.time()
            if now - last_decay >= 0.18:
                progress = max(0, progress - 2)
                last_decay = now

            time.sleep(0.03)

    return progress >= 100


def small_fish_pool(rod_level):
    if rod_level == 1:
        return [fish for fish in FISHING_CATCHES if fish.get("size") == "small"]
    return FISHING_CATCHES


def big_fish_pool(rod_level):
    return [fish for fish in BIG_FISH if fish["min_rod"] <= rod_level]


def add_catch(data, fish_name):
    shiny = random.random() < 0.05

    if not handbook.add_creature(data, fish_name, shiny=shiny):
        return f"Your aquarium is full, so the {fish_name} swims away."

    shiny_text = " shiny" if shiny else ""
    return f"You caught a{shiny_text} {fish_name}! It has moved into your aquarium."


def resolve_catch(data):
    rod_level = min(max(data.get("rod_level", 1), 1), 5)
    rules = ROD_RULES[rod_level]
    roll = random.random()
    available_big_fish = big_fish_pool(rod_level)

    if roll < SMALL_CHANCE:
        catch = random.choice(small_fish_pool(rod_level))
        return add_catch(data, catch["name"])

    if roll < SMALL_CHANCE + BIG_CHANCE and available_big_fish:
        fish_name = random.choice(available_big_fish)["name"]
        if big_fish_fight():
            return add_catch(data, fish_name)
        return "The big fish broke away before you could reel it in."

    coins = random.randint(*rules["coins"])
    data["coins"] += coins
    return f"You pulled up {coins} coins."


def visit_fishing_island(data, print_header, pause):
    print_header(data, "Fishing Island")

    rod_level = data.get("rod_level", 1)
    rod_name = ROD_RULES.get(rod_level, ROD_RULES[1])["name"]

    print(f"Equipped rod: {rod_name}")
    print("Catch odds after a perfect hook: 35% small catch, 15% big fish, 50% coins.")
    print("If no big fish are available for your rod, that chance becomes coins.\n")

    input("Press Enter to cast...")

    show_fishing_scene()

    if not timing_challenge():
        print("\nThe hook missed the perfect moment. Nothing bites.")
        pause()
        return

    message = resolve_catch(data)
    print(f"\n{message}")
    pause()