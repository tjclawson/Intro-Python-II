from room import Room
from player import Player
from item import Item
from lightsource import LightSource

# Declare all the rooms

room = {
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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# add items
room['outside'].items.append(Item("Bag", "Useless Bag"))
room['outside'].items.append(Item("Whistle", "Useless Whistle"))
room['outside'].items.append(LightSource("Torch", "Torch to help you see"))
room['narrow'].items.append(Item("Book", "Book in a language you can't understand"))
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("one", room["outside"])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
directions = ["e", "w", "s", "n"]


while True:
    current_room = player.current_room
    current_room.is_room_illuminated = False

    if current_room.is_light or current_room.contains_lightsource() or player.has_lightsource():
        current_room.is_room_illuminated = True

    print(current_room)

    user_input = input(">>> ")
    input_list = user_input.split()

    if len(input_list) == 1:
        command = input_list[0]
        if command in directions:
            player.move_player(command)
        elif command == "i" or command == "inventory":
            player.list_inventory()
        elif command == "q":
            break
        else:
            print("Please enter a valid command")

    else:
        action = input_list[0]
        item_name = input_list[1]
        if action == "get" or action == "take":
            picked_item = current_room.get_item(item_name)
            player.pickup_item(picked_item)
        elif action == "drop":
            dropped_item = player.drop_item(item_name)
            current_room.add_item(dropped_item)




