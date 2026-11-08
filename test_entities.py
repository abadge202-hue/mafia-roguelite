import random

from config import BLOCK_FRACTION, ENEMY_TYPES, FLOOR_SCALING
from entities import Character, random_enemy
from items import Item


def test_painkillers_heal_to_full_counts_as_used():
    hero = Character("Test", 100, 10)
    hero.health = 80
    hero.inventory.append(Item("Painkillers", "potion", 30))
    status, gained, item_name = hero.use_potion()
    assert status == "used"
    assert hero.health == 100
    assert gained == 20
    assert hero.inventory == []
    assert item_name == "Painkillers"


def test_use_painkillers_at_full_health():
    hero = Character("Test", 100, 10)
    painkiller = Item("Painkillers", "potion", 30)
    hero.inventory.append(painkiller)
    status, gained, item_name = hero.use_potion()
    assert status == "full"
    assert hero.health == 100
    assert painkiller in hero.inventory
    assert gained == 0
    assert item_name is None


def test_no_painkillers_in_inventory():
    hero = Character("Test", 100, 10)
    hero.health = 50
    status, gained, item_name = hero.use_potion()
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
    for enemy_type in ENEMY_TYPES:
        if enemy_type.name == enemy.name:
            base_health = enemy_type.health
            base_damage = enemy_type.damage
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
    damage, blocked, _crit = attacker.attack(target)
    assert blocked
    assert damage == 100 - target.health


def test_attack_reports_not_blocked_normally():
    attacker = Character("Test", 100, 10)
    target = Character("dummy", 100, 10)
    damage, blocked, _crit = attacker.attack(target)
    assert not blocked
    assert damage == 100 - target.health


def test_use_potion_works_with_any_potion():
    hero = Character("Test", 100, 10)
    hero.health = 50
    hero.inventory.append(Item("Whiskey", "potion", 15))
    status, gained, item_name = hero.use_potion()
    assert status == "used"
    assert hero.health == 65
    assert gained == 15
    assert item_name == "Whiskey"
    assert hero.inventory == []
