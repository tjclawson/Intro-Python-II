from player import Player
from world import World
from battle import Battle

#
# Main
#
# Initialize world
world = World()

# Initialize player using user selected name and set room to outside
print("\nWelcome to Python Adventure!")
user_name = input("\nPlease enter your desired username: ")
player = Player(f"{user_name}", world.room["outside"], 3)


while True:
    player.current_room.is_room_illuminated = False

    if player.current_room.is_light or player.current_room.contains_lightsource() or player.has_lightsource():
        player.current_room.is_room_illuminated = True

    print(player.current_room)

    if player.current_room.monster is not None:
        player = Battle(player, player.current_room.monster).battle()
        if player.hp == 0:
            break
        print(player.current_room)

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
            picked_item = player.current_room.get_item(item_name)
            player.pickup_item(picked_item)
        elif action == "drop":
            dropped_item = player.drop_item(item_name)
            player.current_room.add_item(dropped_item)




