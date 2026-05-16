import json
import os
import select
import shutil
import subprocess
import sys
import termios
import tty

import fishing
import handbook
import quarium
import shop


SAVE_FILE = "aquashell_save.json"
SAVE_VERSION = 6
STARTING_COINS = 35
OLD_STARTERS = {
    "Starter Guppy",
    "Sunny Goldfish",
    "White Swan",
    "Ribbon Eel",
    "Ancient Whale",
    "Paper Ray",
    "Moon Jelly",
    "Tiny Turtle",
}
OLD_FREE_STARTERS = {"Starfish", "Seahorse"}
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
RESET = "\033[0m"

TITLE_ART = r"""
   ___    ____  __  __ ___    _____ __  __ ______ __    __
  /   |  / __ \/ / / //   |  / ___// / / // ____// /   / /
 / /| | / / / / / / // /| |  \__ \/ /_/ // __/  / /   / /
/ ___ |/ /_/ / /_/ // ___ | ___/ / __  // /___ / /___/ /___
/_/  |_/_____/\____//_/  |_|/____/_/ /_//_____//_____//_____/
""".strip("\n")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause(message="Press Enter to continue..."):
    input(f"\n{message}")


def save_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), SAVE_FILE)


def starter_data():
    return {
        "version": SAVE_VERSION,
        "coins": STARTING_COINS,
        "inventory": [{"name": name, "shiny": False} for name in handbook.STARTER_NAMES],
        "rod_level": 1,
        "tank_capacity": 10,
        "capacity_upgrade_count": 0,
        "visits": 0,
    }


def migrate_inventory(inventory, remove_old_free_starters=False):
    entries = []
    skipped_free_starters = set()
    for item in inventory:
        if isinstance(item, dict):
            name = item.get("name")
            shiny = bool(item.get("shiny", False))
        else:
            name = item
            shiny = False

        if (
            remove_old_free_starters
            and name in OLD_FREE_STARTERS
            and name not in skipped_free_starters
        ):
            skipped_free_starters.add(name)
            continue

        if name and name not in OLD_STARTERS and handbook.get_creature(name):
            entries.append({"name": name, "shiny": shiny})

    owned_names = {entry["name"] for entry in entries}
    for name in handbook.STARTER_NAMES:
        if name not in owned_names:
            entries.append({"name": name, "shiny": False})

    return entries


def migrate_save(data):
    previous_version = data.get("version", 0)
    data.setdefault("coins", STARTING_COINS)
    data.setdefault("visits", 0)
    data.setdefault("rod_level", 1)
    data.setdefault("tank_capacity", 10)
    data.setdefault("capacity_upgrade_count", 0)
    data["inventory"] = migrate_inventory(
        data.get("inventory", []),
        remove_old_free_starters=previous_version < 6,
    )
    data["version"] = SAVE_VERSION
    return data


def load_game():
    path = save_path()
    if not os.path.exists(path):
        data = starter_data()
        save_game(data)
        return data

    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError):
        data = starter_data()

    data = migrate_save(data)
    save_game(data)
    return data


def save_game(data):
    with open(save_path(), "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def delete_save(data):
    print_header(data, "Delete Save")
    print("This will erase your coins, fishing rod, visits, and owned creatures.")
    confirmation = input('Type "DELETE" exactly to delete your save: ')

    if confirmation != "DELETE":
        pause("Delete cancelled. Press Enter...")
        return data

    path = save_path()
    if os.path.exists(path):
        os.remove(path)

    new_data = starter_data()
    save_game(new_data)
    data.clear()
    data.update(new_data)
    pause("Save deleted. A fresh aquarium has been created. Press Enter...")
    return data


def color_text(text, color):
    return f"{color}{text}{RESET}"


def centered(text, width=None):
    if width is None:
        width = shutil.get_terminal_size((90, 28)).columns
    return "\n".join(line.center(width) for line in text.splitlines())


def print_title():
    colors = [CYAN, GREEN, YELLOW, MAGENTA, BLUE]
    for index, line in enumerate(centered(TITLE_ART).splitlines()):
        print(colors[index % len(colors)] + line + RESET)


def print_header(data, subtitle):
    clear_screen()
    print_title()
    width = shutil.get_terminal_size((90, 28)).columns
    used = handbook.capacity_used(data)
    limit = handbook.capacity_limit(data)
    stats = (
        f"Coins: {data['coins']} | Creatures: {len(data['inventory'])} | "
        f"Rod Level: {data.get('rod_level', 1)} | Capacity: {used}/{limit}"
    )
    bar = "=" * min(width, 82)
    print(color_text(bar.center(width), CYAN))
    print(color_text(subtitle.center(width), YELLOW))
    print(color_text(stats.center(width), GREEN))
    print(color_text(bar.center(width), MAGENTA))


class RawTerminal:
    def __enter__(self):
        self.fd = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(self.fd)
        tty.setcbreak(self.fd)
        return self

    def __exit__(self, exc_type, exc, traceback):
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)


def read_key():
    if not sys.stdin.isatty():
        return input("\nChoose an option: ").strip()

    while True:
        ready, _, _ = select.select([sys.stdin], [], [], 0.1)
        if ready:
            key = sys.stdin.read(1)
            if key == "\x1b":
                key += sys.stdin.read(2)
            return key


def choose_from_menu(data, options):
    if not sys.stdin.isatty():
        print_header(data, "Main Hall")
        for index, (label, _) in enumerate(options, start=1):
            print(f"{index}. {label}")
        choice = read_key()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1][1]
        return None

    selected = 0
    with RawTerminal():
        while True:
            print_header(data, "Main Hall")
            print(color_text("Use ↑/↓ and press Enter.".center(shutil.get_terminal_size((90, 28)).columns), CYAN))
            print()
            for index, (label, _) in enumerate(options):
                prefix = "  > " if index == selected else "    "
                line = f"{prefix}{label}"
                if index == selected:
                    width = shutil.get_terminal_size((90, 28)).columns
                    print("\033[47m\033[30m" + line.center(width) + RESET)
                else:
                    print(color_text(line.center(width), GREEN))

            key = read_key()
            if key == "\x1b[A":
                selected = (selected - 1) % len(options)
            elif key == "\x1b[B":
                selected = (selected + 1) % len(options)
            elif key in {"\n", "\r"}:
                return options[selected][1]


def lobby(data):
    while True:
        options = [
            ("Travel to Fishing Island", "fishing"),
            ("Enter the Shell Shop", "shop"),
            ("Visit Your Aquarium", "aquarium"),
            ("Open Fish Handbook", "handbook"),
            ("Delete Save", "delete"),
            ("Save and Quit", "quit"),
        ]
        choice = choose_from_menu(data, options)
        if choice == "shop":
            shop.enter_shop(data, print_header, pause)
        elif choice == "fishing":
            fishing.visit_fishing_island(data, print_header, pause)
        elif choice == "aquarium":
            quarium.visit_aquarium(data, pause)
        elif choice == "handbook":
            handbook.show_handbook(data, print_header, pause)
        elif choice == "delete":
            delete_save(data)
        elif choice == "quit":
            save_game(data)
            print("\nYour aquarium has been saved. Goodbye!")
            return
        else:
            pause("Invalid choice. Press Enter to try again...")


def main():
    data = load_game()
    lobby(data)


if __name__ == "__main__":
    main()
