#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]

    Objective: 
        You are being hunted by a monster in a labyrinth-like mansion. You must find a key to and find the door to the Garden to escape. The ravenous beast will surely kill you if you encounter it, however, a weapon may help your survive long enough to heal yourself. If you travel too long after your encounter you may succumb to the beast poison. Good luck! \n    
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + str(rooms[currentRoom]['item']))
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# poisoned status becomes, True if you fight off the beast and survive
poisoned = False

# poison severity is scaled from 0 - 4, with 3 being dead
poison_severity = 0

# your weapon becomes equipped when you find the fire poker
weapon_equipped = False 

## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west'  : 'Study',
                  'item'  : 'lantern'
                },
            'Study' : {
                  'east' : 'Hall',
                  'south': 'Laundry',
                  'item' : ['lotion', 'fire poker']
                },
            'Laundry' : {
                    'north' : 'Study',
                    'east'  : 'Kitchen',
                    'item'  : 'antidote'
                },
            'Kitchen' : {
                  'north'  : 'Hall',
                  'west'   : 'Laundry',
                  'item'   : 'monster'
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'east' : 'Sitting Room',
                  'item' : 'knife'
                },
            'Sitting Room' : {
                'west' : 'Dining Room', 
                'item' : 'key'
                },
            'Garden' : {
                'north' : 'Dining Room'
                }
          }


# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
            # checks to see if you have a weapon
            if "fire poker" or "knife" in inventory:
                weapon_equipped = True
                print('A weapon is equipped!')
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

     ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and weapon_equipped: 
        print('''The monster has attacked you, but you defended yourself with the fire poker to get away.
                You are mortally wounded slowly succumbing to monster\'s poison.
                Better find something to help yourself fast before you pass out.''') 
        poisoned = True
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

    # Logic that handles poisoned player
    if 'antidote' in inventory and poisoned: 
        use_antidote = input('You have an antidote, would you like to use it? (Y/N)> ').lower()
        if use_antidote == 'y':
            inventory.remove('antidote')
            poisoned = False
        else:
            poison_severity += 1
    elif move[0] == 'go' and poisoned:
        poison_severity += 1

    if poison_severity == 4: 
        print('You have succumbed to the monster\'s poison. GAME OVER')
        break

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory:
        print('You escaped the house with the ultra rare key... YOU WIN!')
        break

