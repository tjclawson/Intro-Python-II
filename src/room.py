# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.items = []

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

    def print_room_details(self):
        print(self.name)
        print(self.description)
        print("Items in room")
        for item in self.items:
            print(f"~\t{item.name}: {item.description}")

