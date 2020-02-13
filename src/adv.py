from player import Player
from world import World


#
# Main
#
# Initialize world
world = World()

# Initialize player using user selected name and set room to outside
print("\nWelcome to Python Adventure!")
user_name = input("\nPlease enter your desired username: ")
player = Player(f"{user_name}", world.room["outside"])


while True:
    current_room = player.current_room
    current_room.is_room_illuminated = False

    if current_room.is_light or current_room.contains_lightsource() or player.has_lightsource():
        current_room.is_room_illuminated = True

    print(current_room)

    while current_room.monster is not None:
        print("\nTHERE IS A MONSTER IN THIS ROOM!")
        print(current_room.monster)
        option = input('What will you do? Use "attack" to attack the monster, use "run" to run away: ')
        if option == "run":
            current_room = player.last_room
            player.current_room = player.last_room
        
        print(current_room)

    user_input = input(">>> ")
    input_list = user_input.split()

    if len(input_list) == 1:
        command = input_list[0]
        if command in world.directions:
            player.move_player(command)
        elif command == "i" or command == "inventory":
            player.list_inventory()
        elif command == "help":
            world.help()
        elif command == "q":
            break
        else:
            print('\nPlease enter a valid command, enter "help" to see a list of valid commands')

    else:
        action = input_list[0]
        item_name = input_list[1]
        if action == "get" or action == "take":
            picked_item = current_room.get_item(item_name)
            player.pickup_item(picked_item)
        elif action == "drop":
            dropped_item = player.drop_item(item_name)
            current_room.add_item(dropped_item)




