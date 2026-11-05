import random
from dataclasses import dataclass

from config import ITEM_TYPES


@dataclass
class Item:
    name: str
    item_type: str
    value: int


def random_item():
    """Return a random item: (weapon, armor, potion), weighted by drop chance."""
    pick = random.choices(ITEM_TYPES, k=1, weights=[t.weight for t in ITEM_TYPES])[0]
    return Item(name=pick.name, item_type=pick.item_type, value=pick.value)
