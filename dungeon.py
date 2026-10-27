import random

from config import MAX_ROOMS, MIN_ROOMS, ROOM_TYPES, RoomType,  ROOM_WEIGHTS
from dataclasses import dataclass

@dataclass
class Room:
    room_type: RoomType
    place: str


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
