from data import valid_classes
from character import Character
from exploration import explore
from inventory import manage_inventory

print("Welcome to Random Wanderer!")
name = input("Enter your character's name: ")

print("Choose your class:")
for i, c in enumerate(valid_classes, 1):
    print(f"{i}. {c}")

while True:
    try:
        choice = int(input("Enter the number of your class choice: "))
        if 1 <= choice <= len(valid_classes):
            char_class = valid_classes[choice - 1]
            break
        else:
            print("Invalid number. Try again.")
    except ValueError:
        print("Please enter a valid number.")

player = Character(name, char_class)
in_town = False
player.show_stats()
can_rest = False
while True:
    print("\nMain Menu:")
    print("1. Explore")
    print("2. Rest")
    print("3. View Stats")
    print("4. Inventory")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
       in_town = False # assume your leaving town unless returned
       result = explore(player) # updates based on area
       if isinstance(result, bool):
           in_town = result
           can_rest = not in_town # only allows resting when not in town and it's safe
    elif choice == "2":  # Rest
        if in_town or can_rest:
         heal = 10 + player.level * 2
         mana_regen = 15
         player.hp = min(player.hp + heal, player.max_hp)
         if player.char_class in ["Wizard", "Cleric"]:
             player.mana = min(player.mana + mana_regen, player.max_mana)
         elif player.char_class in ["Fighter", "Rogue"]:
             player.energy = min(player.energy + 10, player.max_energy)  # Optional energy regen
         print(f"You rest and recover {heal} HP and {mana_regen} Mana.")
        else:
         print("You can only rest in towns or safe zones.")
    elif choice == "3":
        player.show_stats()
    elif choice == "4":
        manage_inventory(player)
    elif choice == "5":
        print("Thanks for playing Random Wanderer!")
        break
    else:
        print("Invalid choice. Please choose a number from 1–5.")