
def manage_inventory(player):
    if not player.inventory:
        print("Your inventory is empty.")
        return

    print("\nInventory:", player.inventory)
    item = input("Which item would you like to use or equip? (type exactly or 'cancel'): ")
    if item.lower() == 'cancel':
        return
    if item in player.inventory:
        if player.use_item(item):
            player.inventory.remove(item)
        else:
            player.equip_item(item)
            player.inventory.remove(item)
    else:
        print("Item not found.")