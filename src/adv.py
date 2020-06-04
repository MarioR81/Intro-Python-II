from room import Room
from player import Player
import argparse

parser = argparse.ArgumentParser()
parser.parse_args()

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
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

#
# Main
#

def menu():
    print("To move, type 'n', 's', 'e', or 'w'.")
    print(" ")
    print("To see this menu again, type 'h'.")
    print(" ")
    print("To Quit game, type 'q'.")
    
print("Welcome to the Adventure Game!")
print(" ")
menu()

direction_abbreviations = {
    "n": "north",
    "s": "south",
    "e": "east",
    "w": "west",
    "u": "up",
    "d": "down"
}

direction_adj_phrase = {
    "n": "to the north",
    "s": "to the south",
    "e": "to the east",
    "w": "to the west",
    "u": "above",
    "d": "below"
}

# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'], "Adventurer #1")

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

while True:
    current_room = player.get_location()
    user_input = input("> ").lower()
    input_words = user_input.strip().split(" ")
    
    if (user_input == 'q'):
        break

    elif (user_input == 'h'):
        menu()

    elif (user_input in direction_abbreviations):

        
        next_room = current_room.get_next_room(user_input)

        if next_room:
            player.move_to_location(next_room)
            print("You move " + direction_abbreviations[user_input] + ".")
            next_room.describe()
        else:
            print("There is no exit " + direction_adj_phrase[user_input] + " from here.")

    # else (user_input = )
    #     print("Invalid input!")