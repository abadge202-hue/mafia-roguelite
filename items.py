import random

from config import ITEM_TYPES
from dataclasses import dataclass

@dataclass
class Item:
  name: str
  item_type: str
  value: int


def random_item():
    name, item_type, value = random.choice(ITEM_TYPES)
    return Item(name, item_type, value)
