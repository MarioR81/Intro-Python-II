# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    
    # exits
    n_to = None
    s_to = None
    e_to = None
    w_to = None
    u_to = None
    d_to = None

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def get_next_room(self, direction):

        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        elif direction == "u":
            return self.u_to
        elif direction == "d":
            return self.d_to