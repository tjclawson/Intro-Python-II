from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
room['outside'].items.append(Item("Test1", "Test item"))
room['outside'].items.append(Item("Test2", "Test item"))
room['outside'].items.append(Item("Test3", "Test item"))
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

    print(current_room.name)
    print(current_room.description)
    print("Items in room")
    for i in current_room.items:
        print("~\t" + i.name)

    user_input = input("Enter direction you would like to move, or q to quit: ")
    input_list = user_input.split()
    if len(input_list) == 1:
        if user_input in directions and user_input in current_room.get_valid_directions():
            if user_input == "e":
                player.current_room = current_room.e_to
            elif user_input == "w":
                player.current_room = current_room.w_to
            elif user_input == "n":
                player.current_room = current_room.n_to
            elif user_input == "s":
                player.current_room = current_room.s_to

        elif user_input == "q":
            break
        elif user_input in directions and user_input not in current_room.get_valid_directions():
            print(f"You cannot move to the {user_input} from here")
        else:
            print("Please enter a valid cardinal direction")

    else:
        if input_list[0] == "get" or "take":
            try:
                item = [item for item in current_room.items if item.name == input_list[1]][0]
                player.inventory.append(item)
                current_room.items.remove(item)
            except IndexError:
                print(f"{input_list[1]} is not an item in this room!")

