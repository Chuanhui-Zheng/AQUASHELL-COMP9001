import shutil

import handbook
from handbook import CYAN, GREEN, MAGENTA, RESET, YELLOW, count_owned, preview_sprite


ROD_UPGRADES = [
    {"level": 2, "name": "Copper Rod", "price": 40},
    {"level": 3, "name": "Silver Rod", "price": 85},
    {"level": 4, "name": "Golden Rod", "price": 150},
    {"level": 5, "name": "Mythic Rod", "price": 260},
]

ROD_NAMES = {
    1: "Basic Rod",
    2: "Copper Rod",
    3: "Silver Rod",
    4: "Golden Rod",
    5: "Mythic Rod",
}


def color(text, value):
    return f"{value}{text}{RESET}"


def capacity_price(data):
    return 25 + data.get("capacity_upgrade_count", 0) * 15


def enter_shop(data, print_header, pause):
    while True:
        print_header(data, "Shell Shop")
        rod_level = data.get("rod_level", 1)
        used = handbook.capacity_used(data)
        limit = handbook.capacity_limit(data)
        print(color(center(f"Current fishing rod: {ROD_NAMES.get(rod_level, 'Basic Rod')}"), GREEN))
        print(color(center(f"Aquarium capacity: {used}/{limit}"), CYAN))
        print()

        print(color(center("Creatures"), MAGENTA))
        for index, item in enumerate(handbook.SHOP_STOCK, start=1):
            owned = count_owned(data, item["name"])
            owned_text = f" | owned {owned}" if owned else ""
            line = f"{index}. {item['name']:<16} {item['price']:>3} coins{owned_text}   {preview_sprite(item)}"
            print(center(line))

        print()
        print(color(center("Fishing Rods"), MAGENTA))
        for upgrade in ROD_UPGRADES:
            label = f"R{upgrade['level']}"
            if rod_level >= upgrade["level"]:
                line = f"{label}. {upgrade['name']:<16} owned"
            elif rod_level + 1 == upgrade["level"]:
                line = f"{label}. {upgrade['name']:<16} {upgrade['price']:>3} coins"
            else:
                line = f"{label}. {upgrade['name']:<16} locked"
            print(center(line))

        print()
        print(color(center("Aquarium"), MAGENTA))
        print(center(f"C. Add 5 capacity for {capacity_price(data)} coins"))

        print()
        print(color(center("Sell Fish"), MAGENTA))
        print_sellable_fish(data)
        print(center('Type: sell number quantity    Example: sell 2 1'))
        print(center("Shiny fish cannot be sold."))
        print()
        print(color(center(" Press Enter to quit the shop. "), YELLOW))

        choice = input("\nChoose an item: ").strip()
        lowered = choice.lower()
        if choice == "":
            return

        if lowered.startswith("sell "):
            sell_fish(data, choice[5:].strip(), pause)
            continue

        if lowered == "c":
            buy_capacity(data, pause)
            continue

        if lowered.startswith("r") and lowered[1:].isdigit():
            upgrade_rod(data, int(lowered[1:]), pause)
            continue

        if not choice.isdigit() or not 1 <= int(choice) <= len(handbook.SHOP_STOCK):
            pause("That shelf is empty. Press Enter...")
            continue

        item = handbook.SHOP_STOCK[int(choice) - 1]
        if data["coins"] < item["price"]:
            pause("Not enough coins. Press Enter...")
            continue
        if not handbook.add_creature(data, item["name"]):
            pause("Your aquarium is full. Buy more capacity first. Press Enter...")
            continue

        data["coins"] -= item["price"]
        pause(f"You bought {item['name']}! Press Enter...")


def buy_capacity(data, pause):
    price = capacity_price(data)
    if data["coins"] < price:
        pause("Not enough coins for more capacity. Press Enter...")
        return

    data["coins"] -= price
    data["tank_capacity"] = data.get("tank_capacity", 10) + 5
    data["capacity_upgrade_count"] = data.get("capacity_upgrade_count", 0) + 1
    pause("Aquarium capacity increased by 5. Press Enter...")


def center(text):
    return text.center(shutil.get_terminal_size((90, 28)).columns)


def sellable_items(data):
    items = []
    names = sorted({handbook.normalize_entry(item)["name"] for item in data.get("inventory", [])})
    for name in names:
        creature = handbook.get_creature(name)
        if not creature or creature.get("sell_price", 0) <= 0:
            continue
        quantity = count_owned(data, name, shiny=False)
        if quantity <= 0:
            continue
        items.append((name, quantity, creature.get("sell_price", 0)))
    return items


def print_sellable_fish(data):
    items = sellable_items(data)
    if not items:
        print(center("No normal sellable fish right now."))
        return

    for index, (name, quantity, price) in enumerate(items, start=1):
        line = f"{index}. {name} [{quantity}] {price} coins"
        print(center(line))


def parse_sell_command(command, items):
    parts = command.split()
    if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
        return None, None

    index = int(parts[0])
    if not 1 <= index <= len(items):
        return None, None

    return items[index - 1][0], int(parts[1])


def sell_fish(data, command, pause):
    items = sellable_items(data)
    name, quantity = parse_sell_command(command, items)
    if not name or quantity <= 0:
        pause("Use: sell number quantity. Press Enter...")
        return

    creature = handbook.get_creature(name)
    normal_owned = count_owned(data, name, shiny=False)
    if normal_owned <= 0:
        pause("You do not have a normal sellable fish with that name. Press Enter...")
        return
    if quantity > normal_owned:
        pause(f"You only have {normal_owned} normal {name}. Press Enter...")
        return

    removed = handbook.remove_creatures(data, name, quantity, allow_shiny=False)
    coins = creature.get("sell_price", 0) * removed
    data["coins"] += coins
    pause(f"Sold {removed} {name} for {coins} coins. Press Enter...")


def upgrade_rod(data, target_level, pause):
    current_level = data.get("rod_level", 1)
    upgrade = next((item for item in ROD_UPGRADES if item["level"] == target_level), None)

    if not upgrade:
        pause("That fishing rod does not exist. Press Enter...")
        return
    if target_level <= current_level:
        pause(f"You already own the {upgrade['name']}. Press Enter...")
        return
    if target_level != current_level + 1:
        pause("You must buy fishing rods in order. Press Enter...")
        return
    if data["coins"] < upgrade["price"]:
        pause("Not enough coins for that rod. Press Enter...")
        return

    data["coins"] -= upgrade["price"]
    data["rod_level"] = target_level
    pause(f"You upgraded to the {upgrade['name']}! Press Enter...")
