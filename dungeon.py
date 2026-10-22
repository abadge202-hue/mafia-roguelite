from config import ROOM_TYPES, ROOM_WEIGHTS, MIN_ROOMS, MAX_ROOMS
import random


class Room:
    def __init__(self, room_type, place):
        self.room_type = room_type
        self.place = place



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
    count = random.randint(MIN_ROOMS, MAX_ROOMS)
    return [
        Room(
            random.choices(ROOM_TYPES, weights=ROOM_WEIGHTS)[0],
            random.choice(PLACE_TYPES),
        )
        for _ in range(count)
    ]
