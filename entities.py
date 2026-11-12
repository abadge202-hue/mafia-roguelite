import random

from config import (
    BLOCK_FRACTION,
    BOSS_TYPES,
    CRIT_MULTIPLIER,
    DAMAGE_SPREAD,
    ENEMY_TYPES,
    FLOOR_SCALING,
    ItemCategory,
)


class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.max_health = health
        self.defending = False
        self.winding_up = False
        self.defense = 0
        self.inventory = []

    def heal(self, amount):
        """Heal by amount, capped at max health; return the health actually gained."""
        old_health = self.health
        self.health = min(self.max_health, self.health + amount)
        gained_health = self.health - old_health
        return gained_health

    def use_potion(self):
        """Use one potion; return (status, health gained, item name or None)."""
        if self.health == self.max_health:
            return "full", 0, None
        for item in self.inventory:
            if item.item_type == ItemCategory.POTION:
                gained_health = self.heal(item.value)
                self.inventory.remove(item)
                return "used", gained_health, item.name
        return "none", 0, None

    def pick_up(self, item):
        """Apply an item: weapons add damage, armor adds defense, potions go to the inventory"""
        if item.item_type == ItemCategory.POTION:
            self.inventory.append(item)
        elif item.item_type == ItemCategory.WEAPON:
            self.damage += item.value
        elif item.item_type == ItemCategory.ARMOR:
            self.defense += item.value

    def attack(self, target):
        """Hit the target and return (damage dealt, whether it was blocked, whether it was a critical hit)."""
        damage_dealt = max(
            1, random.randint(self.damage - DAMAGE_SPREAD, self.damage + DAMAGE_SPREAD)
        )
        crit = False
        if self.winding_up:
            damage_dealt = int(damage_dealt * CRIT_MULTIPLIER)
            crit = True
            self.winding_up = False
        damage_dealt = max(1, damage_dealt - target.defense)
        blocked = False
        if target.defending:
            blocked = True
            damage_dealt = int(damage_dealt * BLOCK_FRACTION)
            target.defending = False
        target.health = max(0, target.health - damage_dealt)
        return damage_dealt, blocked, crit


def create_boss(floor_number):
    """Return a specific boss for the given floor"""
    boss_type = BOSS_TYPES[floor_number - 1]
    return Character(boss_type.name, boss_type.health, boss_type.damage)


def random_enemy(floor_number):
    """Return a random enemy with stats scaled up for the given floor"""
    pick = random.choices(ENEMY_TYPES, k=1, weights=[t.weight for t in ENEMY_TYPES])[0]
    floor_multiplier = 1 + (floor_number - 1) * FLOOR_SCALING
    health = round(pick.health * floor_multiplier)
    damage = round(pick.damage * floor_multiplier)
    return Character(pick.name, health, damage)
