import random


class Room:
    def __init__(self, room_type, place):
        self.room_type = room_type
        self.place = place


ROOM_TYPES = ["enemy", "treasure", "empty", "rest"]
ROOM_WEIGHTS = [50, 15, 15, 20]
PLACE_TYPES = [
    "a buzzing nightclub",
    "a dimly lit alley",
    "the back of a shipping warehouse",
    "a shipping container",
    "the lobby of a highrise building",
]

BOSS_ROOMS = [
    "the club manager's office",
    "a luxurious penthouse suite",
    "a highrise helipad",
]


def generate_floor():
    count = random.randint(5, 8)
    return [
        Room(
            random.choices(ROOM_TYPES, weights=ROOM_WEIGHTS)[0],
            random.choice(PLACE_TYPES),
        )
        for _ in range(count)
    ]
