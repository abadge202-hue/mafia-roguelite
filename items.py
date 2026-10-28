import random
from dataclasses import dataclass

from config import ITEM_TYPES


@dataclass
class Item:
    name: str
    item_type: str
    value: int


def random_item():
    """Return a random item: weapon, armor, potion."""
    name, item_type, value = random.choice(ITEM_TYPES)
    return Item(name, item_type, value)
