import random
def shop_menu(shop_type):
    print("\nShop Menu:")
    if shop_type == "Weapon":
        print("1. Weapon Upgrade - 50 gold")
    elif shop_type == "Armor":
        print("1. Armor Upgrade - 50 gold")
    elif shop_type == "Magic":
        print("1. Healing Potion - 20 gold")
        print("2. Mana Potion - 25 gold")
    print("8. Sell an Item")
    print("9. Exit Shop")

def shop_interaction(player, shop_type):
    if shop_type == "Weapon":
        shop_items = {
            "1": ("Weapon Upgrade", 50)
        }
    elif shop_type == "Armor":
        shop_items = {
            "1": ("Armor Upgrade", 50)
        }
    elif shop_type == "Magic":
        shop_items = {
            "1": ("Healing Potion", 20),
            "2": ("Mana Potion", 25)
        }
    else:
        shop_items = {}

    while True:
        shop_menu(shop_type)
        choice = input("What would you like to buy? ")

        if choice == "9":
            print("You leave the shop.")
            break

        elif choice == "8":
            sell_from_inventory(player)

        if choice in shop_items:
            item_name, cost = shop_items[choice]
            if player.gold >= cost:
                player.gold -= cost
                if "Upgrade" in item_name:
                    print(f"You paid {cost} gold for a {item_name.lower()}.")
                    # Placeholder for upgrade effect
                else:
                    player.inventory.append(item_name)
                    print(f"You bought a {item_name}.")
            else:
                print("You don't have enough gold.")
        else:
            print("Invalid option.")

def sell_from_inventory(player):
    if not player.inventory:
        print("You have nothing to sell.")
        return

    print("Your Inventory:")
    for i, item in enumerate(player.inventory, 1):
        print(f"{i}. {item}")

    try:
        selection = int(input("Enter the number of the item to sell (or 0 to cancel): "))
        if selection == 0:
            return
        item = player.inventory.pop(selection - 1)
        gold_value = random.randint(10, 30)
        player.gold += gold_value
        print(f"You sold {item} for {gold_value} gold.")
    except (ValueError, IndexError):
        print("Invalid selection.")