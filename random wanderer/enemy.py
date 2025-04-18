import random

class Enemy:
    def __init__(self, name, base_hp, base_damage, xp_reward, gold_reward, tags=None):
        self.name = name
        self.base_hp = base_hp
        self.base_damage = base_damage
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward
        self.tags = tags if tags else []
        self.hp = base_hp
        self.damage = base_damage

    def scale_for_level(self, level):
        self.hp = self.base_hp + level * 10
        self.damage = self.base_damage + level * 2

    def is_tagged(self, tag):
        return tag in self.tags

# Basic enemy definitions
def get_enemy_list():
    return [
        Enemy("Goblin", base_hp=30, base_damage=5, xp_reward=50, gold_reward=10),
        Enemy("Skeleton", base_hp=40, base_damage=7, xp_reward=60, gold_reward=12, tags=["undead"]),
        Enemy("Orc", base_hp=50, base_damage=10, xp_reward=80, gold_reward=15),
        Enemy("Dark Mage", base_hp=35, base_damage=12, xp_reward=90, gold_reward=20, tags=["caster"]),
        Enemy("Bandit", base_hp=45, base_damage=9, xp_reward=70, gold_reward=18),
        Enemy("Bat", base_hp=15, base_damage=3, xp_reward=25, gold_reward=5),
        Enemy("Bear", base_hp=90, base_damage=18, xp_reward=140, gold_reward=36),
        Enemy("Giant Spider", base_hp=50, base_damage=9, xp_reward=70, gold_reward=15)
    ]

# Optionally select a random enemy

def get_random_enemy(level):
    enemy = random.choice(get_enemy_list())
    enemy.scale_for_level(level)
    return enemy