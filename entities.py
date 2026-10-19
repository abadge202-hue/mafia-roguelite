import random


class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.max_health = health
        self.defending = False
        self.defense = 0
        self.inventory = []

    def heal(self):
        heal_amount = self.max_health // 2
        old_health = self.health
        self.health = min(self.max_health, self.health + heal_amount)
        gained_health = self.health - old_health
        if gained_health == 0:
            print(f"{self.name} is already at full health!")
        else:
            print(
                f"{self.name} heals for {gained_health}. Current health: {self.health}/{self.max_health}"
            )

    def use_painkillers(self):
        for item in self.inventory:
            if self.health == self.max_health:
                print(f"{self.name} is already at full health!")
                return False
            if item.item_type == "potion" and item.name == "Painkillers":
                heal_amount = item.value
                old_health = self.health
                self.health = min(self.max_health, self.health + heal_amount)
                gained_health = self.health - old_health
                self.inventory.remove(item)
                if self.health == self.max_health:
                    print(f"{self.name} is already at full health!")
                    return False
                print(
                    f"{self.name} uses {item.name} and heals for {gained_health}. Current health: {self.health}/{self.max_health}"
                )
                return True
            if self.health == self.max_health:
                print(f"{self.name} is already at full health!")
                return False
        print(f"{self.name} has no Painkillers to use!")
        return False

    def pick_up(self, item):
        if item.item_type == "potion":
            self.inventory.append(item)
            print(f"{self.name} picked up {item.name}!")
        elif item.item_type == "weapon":
            self.damage += item.value
            print(
                f"{self.name} picked up {item.name}! Damage increased by {item.value}."
            )
        elif item.item_type == "armor":
            self.defense += item.value
            print(
                f"{self.name} picked up {item.name}! Defense increased by {item.value}."
            )

    def attack(self, target):
        damage_dealt = max(1, random.randint(self.damage - 2, self.damage + 2))
        damage_dealt = max(1, damage_dealt - target.defense)
        if target.defending:
            print(f"{self.name} attacks {target.name} for {damage_dealt}!")
            damage_dealt = damage_dealt // 2
            print(f"{target.name} is defending! Damage is reduced to {damage_dealt}.")
            target.defending = False
        target.health = max(0, target.health - damage_dealt)
        print(f"{self.name} hits {target.name} for {damage_dealt}")

        if target.health > 0:
            print(f"{target.name} has {target.health} health remaining.")
        else:
            print(f"{target.name} has been defeated!")


ENEMY_TYPES = [("Associate", 20, 2), ("Soldier", 25, 3), ("Capo", 35, 5)]
BOSS_TYPES = [("Underboss", 75, 8)]


def create_boss():
    name, health, damage = BOSS_TYPES[0]
    return Character(name, health, damage)


def random_enemy(floor_number):
    name, health, damage = random.choice(ENEMY_TYPES)
    floor_multiplier = 1 + (floor_number - 1) * 0.2
    health = round(health * floor_multiplier)
    damage = round(damage * floor_multiplier)
    return Character(name, health, damage)
