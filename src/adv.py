from room import Room
from player import Player
from object import Object

# ----------------- Declare all the objects -------------------
torch = Object("torch", "A firestick.", True)
match = Object("match", "A wooden, strike-anywhere match")
shovel = Object("shovel", "A bright yellow, plastic, toy shovel.")
watch = Object("wristwatch", "An elegant timekeeping device.")

# ------------------ Place all the objects --------------------


# ----------------- Declare all the rooms -------------------
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [shovel]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [watch]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# ---------------------- Make the map --------------------------

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
player = Player('Bob', room['outside'], [torch, match])

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
    current_room = player.current_room
    print()
    print(current_room.name)
    print(current_room.description)

    command = input("Next move? ").split(" ")

    if command[0] == 'q' or command[0] == "quit" or command[0] == "exit":
        exit(0)

    if command[0] == 'n' or command[0] == "north":
        if current_room.n_to is None:
            print("That leads nowhere.")
        else:
            player.current_room = current_room.n_to

    if command[0] == 's' or command[0] == "south":
        if current_room.s_to is None:
            print("That leads nowhere.")
        else:
            player.current_room = current_room.s_to

    if command[0] == 'e' or command[0] == "east":
        if current_room.e_to is None:
            print("That leads nowhere.")
        else:
            player.current_room = current_room.e_to

    if command[0] == 'w' or command[0] == "west":
        if current_room.w_to is None:
            print("That leads nowhere.")
        else:
            player.current_room = current_room.w_to

    if command[0] == "look":
        if(len(command) == 1):
            if len(current_room.contents) == 0:
                print("There is nothing to interact with here.")
            else:
                print("You look around and see these items:")
                for item in current_room.contents:
                    print(item.name)

        else:
            print("You're looking for a mysterious {} object.".format(
                command[-1]))

    if command[0] == "inventory":
        if len(player.inventory) == 0:
            print("You aren't carrying anything.")
        else:
            print("You are carrying:")
            for item in player.inventory:
                print(item.name)
                # print(item.name for item in player.inventory)

    if command[0] == "get":
        # Remove from room
        #    if room.contents: # contains item
        #        Remove it.
        #        Add it to the player's inventory.
