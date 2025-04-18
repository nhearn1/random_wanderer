import random
from enemy import get_random_enemy

def fight(player):
    enemy = get_random_enemy(player.level)
    print(f"A wild {enemy.name} appears!")

    while enemy.hp > 0 and player.hp > 0:
        player.regenerate_resources()
        print(f"\n{player.name} HP: {player.hp}, Energy: {player.energy}, Mana: {player.mana}")
        print(f"{enemy.name} HP: {enemy.hp}")

        print("\nChoose your action:")
        print("1. Attack")
        print("2. Use Ability")
        print("3. Inventory")
        print("4. Run")
        action = input("Enter the number of your choice: ")

        if action == "1":
            base = 5 if player.weapon else 0
            dmg = base + player.strength + random.randint(1, 10)
            enemy.hp -= dmg
            print(f"You strike the {enemy.name} for {dmg} damage!")

        elif action == "2":
            if hasattr(player, 'class_action'):
                player.class_action(enemy)
            else:
                print("You don't have any special abilities.")

        elif action == "3":
            print("Inventory:", player.inventory)
            item = input("Use an item or type 'cancel': ")
            if item in player.inventory:
                if player.use_item(item):
                    player.inventory.remove(item)
                else:
                    print("That item can't be used now.")

        elif action == "4":
            print("You run from the battle!")
            return

        else:
            print("Invalid action.")

    if enemy.hp > 0:
    # 1. Unbreakable Will (no damage at all)
        if getattr(player, "invulnerable", False):
            print("You are immune to all damage this turn! (Unbreakable Will)")
            player.invulnerable = False
            return

    # 2. Evasion (completely dodge the hit)
    if getattr(player, "evasion", False):
        print("You evade the attack completely!")
        player.evasion = False
        return

    # 3. Roll damage
    dmg = max(0, random.randint(5, enemy.damage))

    # 4. Arcane Shield (75% reduction)
    if getattr(player, "shielded", False):
        dmg = dmg // 4
        player.shielded = False
        print("Arcane Shield reduces the incoming damage!")

    # 5. Divine Barrier (50% reduction)
    elif getattr(player, "barrier", False):
        dmg = dmg // 2
        player.barrier = False
        print("Divine Barrier reduces the incoming damage!")

    # 6. Defensive Stance (Fighter, 50% reduction)
    elif getattr(player, "defending", False):
        dmg = dmg // 2
        player.defending = False
        print("Your Defensive Stance reduces the incoming damage!")

    # 7. Apply damage
    player.hp -= dmg
    print(f"The {enemy.name} hits you for {dmg} damage!")
    if player.hp > 0:
        print(f"You defeated the {enemy.name}!")
        player.gain_experience(enemy.xp_reward)
        player.gold += enemy.gold_reward
        print(f"You looted {enemy.gold_reward} gold!")
    else:
        print("You were defeated...")
