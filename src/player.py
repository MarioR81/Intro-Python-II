# Write a class to hold player information, e.g. what room they are in
# currently.

import sys
class Player:

    def __init__(self, starting_room, name):
        self.current_room = starting_room
        self.name = name
        self.inventory = []

    def get_location(self):
        return self.current_room

    def move_to_location(self, next_room):
        self.current_room = next_room
