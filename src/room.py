# Implement a class to hold room information. This should have name and
# description attributes.
from lightsource import LightSource


class Room:
    def __init__(self, name, description, is_light):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.items = []
        self.is_light = is_light
        self.is_room_illuminated = is_light

    def __str__(self):
        details = ""
        if self.is_room_illuminated:
            details += f"\n{self.name}\n\n"
            details += f"{self.description}\n\n"

            if len(self.items) != 0:
                details += "Items in room\n"
                for item in self.items:
                    details += f"~\t{item.name}: {item.description}\n"
            else:
                details += "There are no items in this room"
        else:
            details = "It's pitch black!"
        return details

    def get_valid_directions(self):
        directions_list = []
        if self.n_to is not None:
            directions_list.append("n")
        if self.s_to is not None:
            directions_list.append("s")
        if self.e_to is not None:
            directions_list.append("e")
        if self.w_to is not None:
            directions_list.append("w")
        return directions_list

    def add_item(self, item):
        if item is not None:
            self.items.append(item)

    def remove_item(self, item_name):
        try:
            item = None
            for i in self.items:
                if i.name == item_name:
                    item = i
                    break
            self.items.remove(item)
        except IndexError:
            print(f"{item_name} is not in this room!")

    def get_item(self, item_name):
        if self.is_room_illuminated:
            try:
                item = None
                for i in self.items:
                    if i.name == item_name:
                        item = i
                        break
                self.items.remove(item)
                return item
            except ValueError:
                print(f"{item_name} is not in this room!")
        else:
            print("Good luck finding that in the dark!")

    def contains_lightsource(self):
        result = False
        for item in self.items:
            if isinstance(item, LightSource):
                result = True
                break
        return result

