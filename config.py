HERO_NAME = "Amanda"
HERO_HEALTH = 100
HERO_DAMAGE = 10
ENEMY_TYPES = [("Associate", 20, 2), ("Soldier", 25, 3), ("Capo", 35, 5)]
BOSS_TYPES = [("Enforcer", 45, 6), ("Consigliere", 60, 8), ("Underboss", 75, 10)]
ITEM_TYPES = [
    ("Brass knuckles", "weapon", 3),
    ("an Overcoat", "armor", 2),
    ("Painkillers", "potion", 30),
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
