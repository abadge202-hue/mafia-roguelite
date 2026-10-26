from entities import Character
from items import Item


def test_painkillers_heal_to_full_counts_as_used():
    hero = Character("Test", 100, 10)
    hero.health = 80
    hero.inventory.append(Item("Painkillers", "potion", 30))
    assert hero.use_painkillers() is True
    assert hero.health == 100
    assert hero.inventory == []


def test_use_painkillers_at_full_health():
    hero = Character("Test", 100, 10)
    painkiller = Item("Painkillers", "potion", 30)
    hero.inventory.append(painkiller)
    assert hero.use_painkillers() is False
    assert hero.health == 100
    assert painkiller in hero.inventory


def test_no_painkillers_in_inventory():
    hero = Character("Test", 100, 10)
    hero.health = 50
    assert hero.use_painkillers() is False
    assert hero.health == 50


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
