from room import Room
from item import Item
from lightsource import LightSource

class World:
    def __init__(self):
        self.directions = ["e", "w", "s", "n"]
        self.room = {
            'outside': Room("Outside Cave Entrance",
                            "North of you, the cave mount beckons", True),

            'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
        passages run north and east.""", True),

            'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
        into the darkness. Ahead to the north, a light flickers in
        the distance, but there is no way across the chasm.""", True),

            'narrow': Room("Narrow Passage", """The narrow passage bends here from west
        to north. The smell of gold permeates the air.""", False),

            'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
        chamber! Sadly, it has already been completely emptied by
        earlier adventurers. The only exit is to the south.""", False),
        }

        # Link rooms together

        self.room['outside'].n_to = self.room['foyer']
        self.room['foyer'].s_to = self.room['outside']
        self.room['foyer'].n_to = self.room['overlook']
        self.room['foyer'].e_to = self.room['narrow']
        self.room['overlook'].s_to = self.room['foyer']
        self.room['narrow'].w_to = self.room['foyer']
        self.room['narrow'].n_to = self.room['treasure']
        self.room['treasure'].s_to = self.room['narrow']

        # add items
        self.room['outside'].items.append(Item("Bag", "Useless Bag"))
        self.room['outside'].items.append(Item("Whistle", "Useless Whistle"))
        self.room['outside'].items.append(LightSource("Torch", "Torch to help you see"))
        self.room['narrow'].items.append(Item("Book", "Book in a language you can't understand"))

    def help(self):
        print('\nMove with "n", "s", "e", and "w"')
        print('Check your inventory with "i" or "inventory"')
        print('Pickup items by with "take <item_name>" or "get <item_name>"')
        print('Drop items by with "drop <item_name>"')
