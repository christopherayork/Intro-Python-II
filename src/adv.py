from room import Room
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

room['outside'].add_item(Item('Iron_Sword', 'This is a sword forged from iron. Fairly sturdy, sharp enough for '
                                            'general combat.'))
room['foyer'].add_item(Item('Wax_Candle', 'This is a candle made of wax. It produces a small amount of light.'))
room['overlook'].add_item(Item('Iron_Shield', 'An iron shield built for protection.'))
room['narrow'].add_item(Item('Dusty_Tome', 'A very old looking tome. It may be useful for something...'))
room['treasure'].add_item(Item('Golden_Dagger', 'A dagger adorned with gold. It looks very expensive, but it\'s '
                                                'combat ability is up for debate.'))


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
from player import Player

# Make a new player object that is currently in the 'outside' room.

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
validMovement = ['n', 'north', 'e', 'east', 's', 'south', 'w', 'west']


def app():
    running = True
    player1 = Player('Player1', room['outside'])
    msg = False
    while running:
        print(player1.room)
        msg = input()
        if msg == '':
            continue
        elif msg == 'q':
            running = False
        elif msg in validMovement:
            player1.move(msg)
        elif 'grab' in msg:
            args = msg.split(' ')
            if len(args) < 2:
                print('You must specify what to grab')
                continue
            player1.grab(args[1])
            continue
        elif 'drop' in msg:
            args = msg.split(' ')
            if len(args) < 2:
                print('You must specify what to drop')
                continue
            player1.drop(args[1])
            continue
        elif msg == 'i' or msg == 'inventory':
            player1.inventory()


app()
