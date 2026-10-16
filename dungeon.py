import random


class Room:
    def __init__(self, room_type, place):
        self.room_type = room_type
        self.place = place


ROOM_TYPES = ["enemy", "treasure", "empty", "rest"]
PLACE_TYPES = [
    "a buzzing nightclub",
    "a dimly lit alley",
    "the back of a shipping warehouse",
    "a shipping container",
    "the lobby of a highrise building",
]

BOSS_ROOMS = ["a luxurious penthouse"]


def generate_floor():
    count = random.randint(5, 8)
    return [
        Room(random.choice(ROOM_TYPES), random.choice(PLACE_TYPES))
        for _ in range(count)
    ]
