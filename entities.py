import random


class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.defending = False

    def attack(self, target):
        damage_dealt = random.randint(self.damage - 2, self.damage + 2)
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