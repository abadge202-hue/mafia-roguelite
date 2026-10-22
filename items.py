from config import ITEM_TYPES
import random


class Item:
    def __init__(self, name, item_type, value):
        self.name = name
        self.item_type = item_type
        self.value = value





def random_item():
    name, item_type, value = random.choice(ITEM_TYPES)
    return Item(name, item_type, value)
