import random

from config import BLOCK_FRACTION, ENEMY_TYPES, FLOOR_SCALING
from entities import Character, random_enemy
from items import Item


def test_painkillers_heal_to_full_counts_as_used():
    hero = Character("Test", 100, 10)
    hero.health = 80
    hero.inventory.append(Item("Painkillers", "potion", 30))
    status, gained, item_name = hero.use_painkillers()
    assert status == "used"
    assert hero.health == 100
    assert gained == 20
    assert hero.inventory == []
    assert item_name is None


def test_use_painkillers_at_full_health():
    hero = Character("Test", 100, 10)
    painkiller = Item("Painkillers", "potion", 30)
    hero.inventory.append(painkiller)
    status, gained, item_name = hero.use_painkillers()
    assert status == "full"
    assert hero.health == 100
    assert painkiller in hero.inventory
    assert gained == 0
    assert item_name is None


def test_no_painkillers_in_inventory():
    hero = Character("Test", 100, 10)
    hero.health = 50
    status, gained, item_name = hero.use_painkillers()
    assert status == "none"
    assert hero.health == 50
    assert gained == 0
    assert item_name is None


def test_heal_does_not_exceed_max():
    hero = Character("Test", 100, 10)
    hero.health = 80
    gained = hero.heal(50)
    assert hero.health == 100
    assert gained == 20


def test_damage_floor_is_one():
    attacker = Character("Test", 100, 10)
    target = Character("dummy", 100, 10)
    target.defense = 100
    attacker.attack(target)
    assert target.health == 99


def test_enemy_floor_scaling():
    enemy = random_enemy(3)
    for name, health, damage in ENEMY_TYPES:
        if name == enemy.name:
            base_health = health
            base_damage = damage
    assert enemy.health == round(base_health * (1 + 2 * FLOOR_SCALING))
    assert enemy.damage == round(base_damage * (1 + 2 * FLOOR_SCALING))


def test_blocked_damage():
    attacker = Character("Test", 100, 10)
    target = Character("dummy", 100, 10)
    random.seed(17)
    attacker.attack(target)
    normal_damage = 100 - target.health
    attacker = Character("Test", 100, 10)
    target = Character("dummy", 100, 10)
    random.seed(17)
    target.defending = True
    attacker.attack(target)
    blocked_damage = 100 - target.health
    assert blocked_damage == int(normal_damage * BLOCK_FRACTION)


def test_attack_reports_blocked_when_defending():
    attacker = Character("Test", 100, 10)
    target = Character("dummy", 100, 10)
    target.defending = True
    damage, blocked = attacker.attack(target)
    assert blocked
    assert damage == 100 - target.health


def test_attack_reports_not_blocked_normally():
    attacker = Character("Test", 100, 10)
    target = Character("dummy", 100, 10)
    damage, blocked = attacker.attack(target)
    assert not blocked
    assert damage == 100 - target.health
