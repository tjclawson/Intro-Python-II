from item import Item


class Weapon(Item):
    def __init__(self, name, description):
        self.name = name
        self.description = description
