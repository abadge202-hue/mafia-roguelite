from typing import NamedTuple

HERO_NAME = "Amanda"
HERO_HEALTH = 100
HERO_DAMAGE = 10
class EnemyType(NamedTuple):
    name: str
    health: int
    damage: int
ENEMY_TYPES = [
    EnemyType(name = "Associate", health = 20, damage = 2),
    EnemyType(name = "Soldier", health = 25, damage = 3),
    EnemyType(name = "Enforcer", health = 35, damage = 5)]
BOSS_TYPES = [
    EnemyType(name = "Capo", health = 45, damage = 6),
    EnemyType(name = "Consigliere", health =  60, damage = 8),
    EnemyType(name = "Underboss", health = 85, damage = 10)]
class ItemType(NamedTuple):
    name: str
    item_type: str
    value: int
ITEM_TYPES = [
    ItemType(name = "Brass knuckles", item_type = "weapon", value = 3),
    ItemType(name = "an Overcoat", item_type = "armor", value = 2),
    ItemType(name = "Painkillers", item_type = "potion", value = 30),
]
ROOM_TYPES = ["enemy", "treasure", "empty", "rest"]
ROOM_WEIGHTS = [50, 15, 15, 20]
MIN_ROOMS = 5
MAX_ROOMS = 8
FLOOR_SCALING = 0.2
DAMAGE_SPREAD = 2
REST_HEAL_FRACTION = 0.5
BLOCK_FRACTION = 0.5
NUM_FLOORS = 3
