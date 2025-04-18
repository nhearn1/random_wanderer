import random

# Predefined valid classes
valid_classes = ["Fighter", "Wizard", "Cleric", "Rogue"]

# Allowed weapons per class
class_weapons = {
    "Fighter": "Iron Sword",
    "Wizard": "Magic Staff",
    "Cleric": "Morning Star",
    "Rogue": "Dagger"
}

# Character Class
class Character:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.level = 1
        self.experience = 0
        self.hp = 100 + 20 * (self.level - 1)
        self.max_hp = self.hp
        self.gold = 50
        self.inventory = []
        self.weapon = None
        self.armor = None
        self.set_stats()
        self.defending = False
        self.shielded = False
        self.evasion = False
        self.invulnerable = False
        self.empowered = False
        self.barrier = False
        #sets mana and energy based off of class
        if self.char_class in ["Wizard", "Cleric"]:
         self.mana = 50 + 10 * (self.level - 1)
         self.max_mana = self.mana
         self.energy = 0
         self.max_energy = 0
        elif self.char_class in ["Fighter", "Rogue"]:
         self.energy = 50 + 10 * (self.level - 1)
         self.max_energy = self.energy
         self.mana = 0
         self.max_mana = 0

    def set_stats(self):
        if self.char_class == "Fighter":
            self.strength = 15
            self.dexterity = 10
        elif self.char_class == "Wizard":
            self.strength = 8
            self.dexterity = 12
        elif self.char_class == "Cleric":
            self.strength = 12
            self.dexterity = 10
        elif self.char_class == "Rogue":
            self.strength = 10
            self.dexterity = 15

    def gain_experience(self, amount):
        self.experience += amount
        print(f"You gained {amount} XP! Total XP: {self.experience}")
        xp_needed = self.level * 100
        if self.experience >= xp_needed:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0
        self.level += 1
        self.experience = 0
        self.max_hp = 100 + 20 * (self.level - 1)
        self.hp = self.max_hp

        if self.char_class in ["Wizard", "Cleric"]:
          self.max_mana = 50 + 10 * (self.level - 1)
          self.mana = self.max_mana
        elif self.char_class in ["Fighter", "Rogue"]:
          self.max_energy = 50 + 10 * (self.level - 1)
          self.energy = self.max_energy
        self.strength += 2
        self.dexterity += 1
        print(f"\nCongratulations! You reached level {self.level}!")
        print("Your stats have increased!\n")
        self.show_stats()

    def regenerate_resources(self):
        energy_gain = 5 + self.level
        self.energy = min(50 + (self.level - 1) * 10, self.energy + energy_gain)
        print(f"You regain {energy_gain} energy. Current Energy: {self.energy}")

    def equip_item(self, item):
        if item.startswith("Weapon: "):
            weapon_name = item[8:]
            if weapon_name == class_weapons.get(self.char_class):
                self.weapon = item
                print(f"You equipped {weapon_name} as your weapon.")
            else:
                print(f"Your class cannot equip the {weapon_name}.")
        elif item.startswith("Armor: "):
            self.armor = item
            print(f"You equipped {item[7:]} as your armor.")
        else:
            print("You can't equip that.")

    def use_item(self, item):
        if item == "Healing Potion":
            self.hp += 30
            print("You used a Healing Potion and restored 30 HP.")
            return True
        elif item == "Mana Potion":
            self.mana += 20
            print("You used a Mana Potion and restored 20 Mana.")
            return True
        return False

    def show_stats(self):
     print(f"\nName: {self.name}")
     print(f"Class: {self.char_class}")
     print(f"Level: {self.level}")
     print(f"XP: {self.experience}")
     print(f"HP: {self.hp} / {self.max_hp}")

     if self.char_class in ["Wizard", "Cleric"]:
        print(f"Mana: {self.mana} / {self.max_mana}")
     elif self.char_class in ["Fighter", "Rogue"]:
        print(f"Energy: {self.energy} / {self.max_energy}")

     print(f"Strength: {self.strength}")
     print(f"Dexterity: {self.dexterity}")
     print(f"Gold: {self.gold}")
     print(f"Weapon: {self.weapon}")
     print(f"Armor: {self.armor}")
     print(f"Inventory: {self.inventory}\n")

    def class_action(self, enemy):
     if self.level < 2:
        print("You need to be at least level 2 to use abilities.")
        return

     if self.char_class == "Fighter":
        print("\nChoose an ability:")
        print("1. Power Strike (10 energy)")
        print("2. Defensive Stance (10 energy)")
        if self.level >=5:
            print("3. Whirwind Slash (20 energy)")
        if self.level >= 10:
            print("4. Last Stand (30 energy)")
        if self.level >= 15:
            print("5. Unvreakable Will (25 Energy)")

        choice = input("Enter ability number: ")

        if choice == "1":
            if self.energy >= 10:
                self.energy -= 10
                damage = self.strength + 10 + random.randint(5, 15)
                enemy.hp -= damage
                print(f"You unleash Power Strike! You deal {damage} damage.")
            else:
                print("Not enough energy.")
        
        elif choice == "2":
            if self.energy >= 10:
                self.energy -= 10
                self.defending = True
                print("You brace yourself. Incoming damage will be reduced.")
            else:
                print("Not enough energy.")
        
        elif choice == "3" and self.level >= 5:
            if self.energy >= 20:
                self.energy -= 20
                total_damage = 0
                for i in range(2):
                    hit = self.strength + random.randint(5, 10)
                    total_damage += hit
                    print(f"whirlwind hit {i+1} deals {hit} damage.")
                enemy.hp -= total_damage
            else:
                print("Not enough energy")

        elif choice == "4" and self.level >= 10:
            if self.energy >=30:
                self.energy -=30
                if self.hp <= 0.5 * (100 + 20 * (self.level -1)):
                    heal = int(0.3 * (100 + 20 * (self.level)))
                    self.hp += heal
                    print(f"Last Stand activates! you restore {heal} HP and feel empowered!")
                    #might add temp damage boost
                else:
                    print("Last Stand only works when you're below 50% HP.")
            else:
                print("Not enough energy.")

        elif choice == "5" and self.level >= 15:
            if self.energy >= 25:
                self.energy -= 25
                self.invulnerable = True
                print("Unvreakable Will! You will take no damage next turn.")
            else:
                print("Not enough energy.")

        else:
            print("Invalid or unavailable ability.")
    
     elif self.char_class == "Wizard":
        print("\nChoose an ability:")
        print("1. Firebolt (10 mana)")
        print("2. Arcane Shield (15 mana)")
        if self.level >= 5:
            print("3. Fronst Nove (15 mana)")
        if self.level >= 10:
            print("4. Meteor Strike (30 mana)")
        if self.level >= 15:
            print("5. Arcane Ascension (25 mana)")

        choice = input("Enter ability number: ")

        if choice == "1":
            if self.mana >= 10:
                self.mana -= 10
                damage = random.randint(10, 25) + self.dexterity

                if self.empowered:
                    damage += 10
                    self.empowered = False
                    print("Arcane Ascension amplifies your Fiebolt!")
                enemy.hp -= damage
                print(f"You cast Firebolt and deal {damage} damage!")
            else:
                print("Not enough mana.")
        elif choice == "2":
            if self.mana >= 15:
                self.mana -= 15
                self.shielded = True
                print("You cast Arcane Shield. Incoming damage will be greatly reduced.")
            else:
                print("Not enough mana.")
        elif choice == "3" and self.level >= 5:
            if self.mana >= 15:
                self.mana -= 15
                enemy.damage = max(1, enemy.damage // 2)
                print("You freeze your foe with froost Nova! Their damage is reduced next turn")
            else:
                print("Not enough mana")
        elif choice == "4" and self.level >= 10:
            if self.mana >= 30:
                self.mana -=20
                damage = random.randint(35,50) + self.dexterity
                if self.empowered:
                    damage += 10
                    self.empowered = False
                    print("Arcane Ascension amplifies your Metor Strike!")
                enemy.hp -= damage
                print(f"A blazing Meteor crashes down! you deal {damage} damage.")
            else:
                print("not enough mana.")
        elif choice == "5" and self.level >= 15:
            if self.mana >= 25:
                self.mana -=25
                self.mana += 20
                self.empowered = True
                print("You sure with energy! Next spell will deal extra damage.")
            else:
                print("Not enough mana.")
        else:
            print("Invalid or unavailable ability.")
     
     elif self.char_class == "Cleric":
        print("\nChoose an ability:")
        print("1. Healing Light (15 mana)")
        print("2. Smite (10 mana)")
        if self.level >= 5:
            print("3. Divine Barrier (20 mana)")
        if self.level >= 10:
            print("4. Mass Heal (35 mana)")
        if self.level >= 15:
            print("5. Judgement (25 mana)")
        choice = input("Enter ability number: ")

        if choice == "1":
            if self.mana >= 15:
                self.mana -= 15
                heal = random.randint(15, 30)
                self.hp += heal
                print(f"You cast Healing Light and restore {heal} HP!")
            else:
                print("Not enough mana.")
        elif choice == "2":
            if self.mana >= 10:
                self.mana -= 10
                damage = random.randint(12, 22) + self.strength
                enemy.hp -= damage
                print(f"You call down divine wrath! Smite deals {damage} damage.")
            else:
                print("Not enough mana.")
        elif choice == "3" and self.level >= 5:
            if self.mana >= 20:
                self.mana -= 20
                self.barrier = True
                print("Divine Barrier surronds you, reducing the next attack by 50%.")
            else:
                print("Not enough mana.")
        elif choice == "4" and self.level >= 10:
            if self.mana >= 35:
                self.mana -= 35
                heal = random.randint(30,50)
                self.hp += heal
                print(f"You unleash Mass Heal and restore {heal} HP to yourself!")
        elif choice == "5" and self.level >= 15:
            if self.mana >= 25:
                self.mana -= 25
                damage = random.randint(30,45) + self.strength
                enemy.hp -= damage
                print(f"Judgement smites your foe for {damage} radiant damage, ignoring defenses!")
            else:
                print("not enough mana.")
        else:
            print("Invalid or unavailable ability.")

     elif self.char_class == "Rogue":
        print("\nChoose an ability:")
        print("1. Sneak Attack (15 energy)")
        print("2. Evasion (10 energy)")
        if self.level >=5:
            print("3. Shadowstep (20 energy)")
        if self.level >=10:
            print("4. Critical Ambust (30 energy)")
        if self.level >=15:
            print("5. Death's Embrace (25 energy)") 
        choice = input("Enter ability number: ")

        if choice == "1":
            if self.energy >= 15:
                self.energy -= 15
                success = random.choice([True, False])
                if success:
                    damage = random.randint(20, 30) + self.dexterity
                    enemy.hp -= damage
                    print(f"You execute a Sneak Attack! It deals {damage} damage.")
                else:
                    print("Your Sneak Attack failed!")
            else:
                print("Not enough energy.")
        elif choice == "2":
            if self.energy >= 10:
                self.energy -= 10
                self.evasion = True
                print("You vanish into the shadows, ready to evade the next attack!")
            else:
                print("Not enough energy.")
        elif choice == "3" and self.level >=5:
            if self.energy >= 20:
                self.energy -= 20
                self.evasion = True
                print("You fade into the shadows. You'll evade the next attack.")
            else:
                print("Not enough energy.")
        elif choice == "4" and self.level >= 10:
            if self.energy >= 30:
                self.energy -= 30
                damage = random.randint(40, 60) + self.dexterity
                enemy.hp -= damage
                print(f"Critical Ambush! Your strike from the shadows for {damage} damage.")
            else:
                print("Not enough energy.")
        elif choice == "5" and self.level >= 15:
            if self.energy >= 25:
                self.energy -= 25
                enemy.damage = max(1, int(enemy.damage * 0.75))
                print("Death's Embrace weakens your enemy's strength permanently!")
            else:
                print("Not enough energey.")
        else:
            print("Invalid or unavailable ability.")