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
