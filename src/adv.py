from room import Room
from player import Player
from item import Item

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

# Create Items

item = {
    'weapon': Item("Weapon", """Generic looking sharp weapon for slaying monsters"""),

    'shield': Item("Shield", """Large piece of wood used to protect yourself.""")
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

#Add Items to rooms

room['outside'].items.append(item['weapon'])
room['foyer'].items.append(item['shield'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

chris = Player("Chris", room['outside'])

direction = ["n", "s", "e", "w"]

choice = " "


# Write a loop that:
while True:

    # * Prints the current room name
    print(f'\n{chris.current_room.name}')
    # * Prints the current description (the textwrap module might be useful here).
    print(chris.current_room.description)
    if len(chris.current_room.items) > 0:
        print("You see something:")
        for item in chris.current_room.items:
            print(item)
    else:
        print("This room has no items")
    # * Waits for user input and decides what to do.
    choice = list(input("""\n(n) - Move North\n(s) - Move South\n(e) - Move East\n(w) - Move West\n(i) - Inventory\n(q) - Quit\n\nWhat would you like to do?: """).split())
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    if len(choice) == 1:
        if choice[0] == "n":
            print("You moved North")
            if chris.current_room.n_to:
                chris.current_room = chris.current_room.n_to
            else:
                print("You can't move in that direction.")

        elif choice[0] == "s":
            print("You moved South")
            if chris.current_room.s_to:
                chris.current_room = chris.current_room.s_to
            else:
                print("You can't move in that direction.")

        elif choice[0] == "e":
            print("You moved East")
            if chris.current_room.e_to:
                chris.current_room = chris.current_room.e_to
            else:
                print("You can't move in that direction.")

        elif choice[0] == "w":
            print("You moved West")
            if chris.current_room.w_to:
                chris.current_room = chris.current_room.w_to
            else:
                print("You can't move in that direction.")

        elif (choice[0] == "i"):
            print("\nInventory: ")
            if len(chris.inventory) > 0:
                for item in chris.inventory:
                    print(item)
            else:
                print("You have no items.")

        # If the user enters "q", quit the game.

        elif choice[0] == "q":
            print("See you next time!")
            quit()

        else:
            print("Invalid command")

    elif len(choice) == 2:
        if (choice[0] == "get") or (choice[0] == "take"):
            for item in chris.current_room.items:
                if item.name == choice[1]:
                    chris.inventory.append(item)
                    chris.current_room.items.remove(item)
                    item.on_take()
                else:
                    print("No item in this room")
                
        elif choice[0] == "drop":
            for item in chris.inventory:
                if item.name == choice[1]:
                    chris.current_room.items.append(item)
                    chris.inventory.remove(item)
                    item.on_drop()
                else:
                    print("That item is not in your posession.")
