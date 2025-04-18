import random
from combat import fight
from shops import shop_interaction

towns = ["Oakshade", "Silverreach", "Ebon Hollow"]
loot_table = [
    "Healing Potion",
    "Mana Potion",
    "Weapon: Iron Sword",
    "Weapon: Magic Staff",
    "Weapon: Morning Star",
    "Weapon: Dagger",
    "Armor: Leather Armor"
]

def explore(player):
    print("\nYou venture into the unknown...")
    event = random.choices(
        ["monster", "treasure", "town", "nothing"],
        weights=[40, 20, 10, 30],  # total = 100 (or any ratio)
        k=1
    )[0]

    if event == "monster":
        fight(player)
        return False # not safe can't rest
    elif event == "treasure":
        item = random.choice(loot_table)
        player.inventory.append(item)
        player.gain_experience(25)
        print(f"You find a {item} and gain 25 XP!")
        return False # not safe can't rest
    elif event == "town":
        town = random.choice(towns)
        print(f"You discover the town of {town}!")
        return visit_town(player, town) # town handles own state
    else:
        print("The area is quiet... too quiet.")
        return True # safe zone can rest

def visit_town(player, town_name):
    in_town = True
    print(f"\nWelcome to {town_name}!")
    while True:
        print("\nWhere would you like to go?")
        print("1. Pub")
        print("2. Weapon Smith")
        print("3. Armor Smith")
        print("4. Magic Shop")
        print("5. Leave Town")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("You enter the pub.")
            while True:
                print("Pub Menu:")
                print("1. Rest at the inn (25 gold)")
                print("2. Available Quests")
                print("3. Buy a drink")
                print("4. Talk to locals")
                print("5. Return to town menu")
                pub_choice = input("Enter your choice: ")

                if pub_choice == "1":
                    print("The innkeeper offers you a warm bed for 25 gold.")
                    print("1. Yes, rest and recover")
                    print("2. No, return to pub menu")
                    inn_choice = input("Enter your choice: ")

                    if inn_choice == "1":
                        if player.gold >= 25:
                            player.gold -= 25
                            player.hp = player.max_hp
                        if player.char_class in ["Wizard", "Cleric"]:
                            player.mana = player.max_mana
                        elif player.char_class in ["Fighter", "Rogue"]:
                            player.energy = player.max_energy
                            print("You enjoy a warm meal and a soft bed. HP and Mana fully restored.")
                        else:
                            print("You don't have enough gold to stay at the inn.")
                    elif inn_choice == "2":
                        print("You return to the pub common room.")
                    else:
                        print("Invalid option. Returning to pub menu.")

                elif pub_choice == "2":
                    print("Quest board coming soon...")

                elif pub_choice == "3":
                    print("You buy a drink. It's warm and a bit too bitter.")

                elif pub_choice == "4":
                    print("You chat with a few locals. Most speak in hushed tones about monsters nearby.")

                elif pub_choice == "5":
                    print("You leave the pub and return to the town square.")
                    break

                else:
                    print("Invalid choice. Please choose from the pub menu.")

        elif choice == "2":
            print("You visit the Weapon Smith.")
            shop_interaction(player, shop_type="Weapon")

        elif choice == "3":
            print("You visit the Armor Smith.")
            shop_interaction(player, shop_type="Armor")

        elif choice == "4":
            print("You browse through enchanted trinkets in the Magic Shop.")
            shop_interaction(player, shop_type="Magic")

        elif choice == "5":
            print(f"You leave {town_name} and continue your adventure.")
            in_town = False
            return in_town

        else:
            print("Invalid choice.")

    return in_town
