# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

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
            print(f"You do not have {item_name} in your inventory")

