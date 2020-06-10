from room import Room
from player import Player

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

# Make a new player object that is currently in the 'outside' room.

chris = Player("Chris", room['outside'])

direction = ["n", "s", "e", "w"]


# Write a loop that:
while True:

    # * Prints the current room name
    print(f'\n{chris.current_room.name}')
    # * Prints the current description (the textwrap module might be useful here).
    print(chris.current_room.description)
    # * Waits for user input and decides what to do.
    choice = input(
        f"Please choose which direction to go \n(n) - Go North\n(s) - Go South\n(w) - Go West\n(e) - Go East\n(q) - Quit Game: ")
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    if choice == "n":
        print("You moved North")
        if chris.current_room.n_to:
            chris.current_room = chris.current_room.n_to
        else:
            print("You can't move in that direction.")

    elif choice == "s":
        print("You moved South")
        if chris.current_room.s_to:
            chris.current_room = chris.current_room.s_to
        else:
            print("You can't move in that direction.")

    elif choice == "e":
        print("You moved East")
        if chris.current_room.e_to:
            chris.current_room = chris.current_room.e_to
        else:
            print("You can't move in that direction.")

    elif choice == "w":
        print("You moved West")
        if chris.current_room.w_to:
            chris.current_room = chris.current_room.w_to
        else:
            print("You can't move in that direction.")

    # If the user enters "q", quit the game.

    elif choice == "q":
        print("See you next time!")
        quit()

    else:
        print("Invalid command")
