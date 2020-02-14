# Write a class to hold player information, e.g. what room they are in
# currently.
from lightsource import LightSource
from weapon import Weapon
import random


class Player:
    def __init__(self, name, current_room, hp):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        self.last_room = current_room
        self.hp = hp

    def pickup_item(self, item):
        if item is not None:
            self.inventory.append(item)
            item.on_take()

    def drop_item(self, item_name):
        try:
            for i in self.inventory:
                if i.name == item_name:
                    item = i
            self.inventory.remove(item)
            item.on_drop()
            return item
        except UnboundLocalError:
            print(f"\nYou do not have {item_name} in your inventory")

    def list_inventory(self):
        if len(self.inventory) != 0:
            print("\nYour Inventory:")
            for item in self.inventory:
                print(f"~\t{item.name}: {item.description}")
        else:
            print("\nYour inventory is empty!")

    def move_player(self, command):
        if command in self.current_room.get_valid_directions():
            self.last_room = self.current_room
            self.current_room = getattr(self.current_room, f"{command}_to")
        else:
            print(f"\nYou cannot move the {command} from here")

    def has_lightsource(self):
        result = False
        for item in self.inventory:
            if isinstance(item, LightSource):
                result = True
                break
        return result

    def has_weapon(self):
        result = False
        for item in self.inventory:
            if isinstance(item, Weapon):
                result = True
                break
        return result

    def on_attack(self):
        if random.randint(1, 2) == 1:
            print("You were hurt!")
            self.hp -= 1
        else:
            print("The attack missed!")
