import random

from config import (
    BLOCK_FRACTION,
    BOSS_TYPES,
    DAMAGE_SPREAD,
    ENEMY_TYPES,
    FLOOR_SCALING,
)


class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.max_health = health
        self.defending = False
        self.defense = 0
        self.inventory = []

    def heal(self, amount):
        """Heal by amount, capped at max health; return the health actually gained."""
        old_health = self.health
        self.health = min(self.max_health, self.health + amount)
        gained_health = self.health - old_health
        return gained_health

    def use_painkillers(self):
        """Use one painkiller; return (status, health gained, item name or None)."""
        if self.health == self.max_health:
            return "full", 0, None
        for item in self.inventory:
            if item.item_type == "potion" and item.name == "Painkillers":
                gained_health = self.heal(item.value)
                self.inventory.remove(item)
                return "used", gained_health, item.name
        return "none", 0, None

    def pick_up(self, item):
        """Apply an item: weapons add damage, armor adds defense, potions go to the inventory"""
        if item.item_type == "potion":
            self.inventory.append(item)
        elif item.item_type == "weapon":
            self.damage += item.value
        elif item.item_type == "armor":
            self.defense += item.value

    def attack(self, target):
        """Hit the target and return( damage dealt, whether it was blocked)."""
        damage_dealt = max(
            1, random.randint(self.damage - DAMAGE_SPREAD, self.damage + DAMAGE_SPREAD)
        )
        damage_dealt = max(1, damage_dealt - target.defense)
        blocked = False
        if target.defending:
            blocked = True
            damage_dealt = int(damage_dealt * BLOCK_FRACTION)
            target.defending = False
        target.health = max(0, target.health - damage_dealt)
        return damage_dealt, blocked


def create_boss(floor_number):
    """Return a specific boss for the given floor"""
    name, health, damage = BOSS_TYPES[floor_number - 1]
    return Character(name, health, damage)


def random_enemy(floor_number):
    """Return a random enemy with stats scaled up for the given floor"""
    name, health, damage = random.choice(ENEMY_TYPES)
    floor_multiplier = 1 + (floor_number - 1) * FLOOR_SCALING
    health = round(health * floor_multiplier)
    damage = round(damage * floor_multiplier)
    return Character(name, health, damage)
