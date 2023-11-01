import random

# Author: Bryce Schultz
# Define the structure of maps

maps = {
    'Bank': {
        # Defining the connections between the rooms in the Bank map
        'Entry': {'North': 'Teller Counter', 'East': 'Office', 'West': 'Security Desk', 'South': 'Outside'},
        'Security Desk': {'East': 'Entry', 'North': 'Security Room'},
        'Security Room': {'East': 'Teller Counter', 'South': 'Security Desk'},
        'Teller Counter': {'South': 'Entry', 'East': 'Office', 'West': 'Security Room', 'North': 'Vault'},
        'Office': {'West': 'Teller Counter', 'North': 'Break Room', 'East': 'Archive'},
        'Archive': {'West': 'Office', 'East': 'Outside'},
        'Outside': {'North': 'Entry'},
        'Break Room': {'South': 'Office', 'North': 'Entry'},
        'Vault': {'South': 'Teller Counter', 'North': 'Backroom'}
    },
    'Castle': {
        # Defining the connections between the rooms in the Castle map
        'Great Hall': {'North': 'Dining Hall', 'West': 'Guard Room', 'East': 'Hallway', 'South': 'Outside'},
        'Bed Chambers': {'West': 'Hallway'},
        'Kitchen': {'South': 'Dining Hall', 'North': 'Outside'},
        'Dining Hall': {'West': 'Staff Chambers', 'North': 'Kitchen', 'East': 'Hallway'},
        'Guard Room': {'North': 'Staff Chambers', 'East': 'Great Hall'},
        'Cellar': {'West': 'Basement'},
        'Royal Chambers': {'South': 'Hallway'},
        'Staff Chambers': {'West': 'Hallway'},
        'Hallway': {'North': 'Royal Chambers', 'East': 'Bed Chambers', 'South': 'Basement', 'West': 'Great Hall'},
        'Basement': {'North': 'Hallway', 'East': 'Cellar'},
        'Outside': {'North': 'Great Hall', 'South': 'Kitchen', 'East': 'Staff Chambers'}
    },
    'Rival Thieve\'s Guild': {
        # Defining the connections between the rooms in the Rival Thieve's Guild map
        'Entry': {'South': 'Outside', 'North': 'Guard Post'},
        'Guard Post': {'South': 'Entry', 'East': 'Dining Hall', 'North': 'Main Hall'},
        'Dining Hall': {'West': 'Guard Post', 'North': 'Social Room'},
        'Social Room': {'North': 'Planning Room', 'West': 'Main Hall', 'South': 'Dining Hall'},
        'Planning Room': {'South': 'Social Room'},
        'Outside': {'North': 'Entry', 'West': 'Hidden Passageway'},
        'Treasure Room': {'South': 'Main Hall'},
        'Holding Cell': {'South': 'Hidden Passageway', 'East': 'Main Hall'},
        'Hidden Passageway': {'North': 'Holding Cell', 'South': 'Outside'},
        'Main Hall': {'North': 'Treasure Room', 'South': 'Guard Room', 'West': 'Holding Cell', 'East': 'Social Room'}
    }
}
perception = {
    'Bank': {
        # Defining the items found in each room in the Bank map
        'Entry': 'note',
        'Security Desk': '#1_key',
        'Security Room': '',
        'Teller Counter': 'money',
        'Office': '#2_key',
        'Archive': 'documents',
        'Outside': '',
        'Break Room': 'jewelery',
        'Vault': 'gold_bars'
    },
    'Castle': {
        # Defining the items found in each room in the Castle map
        'Great Hall': 'sword',
        'Bed Chambers': 'key',
        'Kitchen': 'gold_spatula',
        'Dining Hall': 'jewelery',
        'Guard Room': 'key_2',
        'Cellar': 'captured_guild_member',
        'Royal Chambers': 'crown',
        'Staff Chambers': '',
        'Hallway': 'gold',
        'Basement': 'lock_box',
        'Outside': ''
    },
    'Rival Thieve\'s Guild': {
        # Defining the items found in each room in the Rival Thieve's Guild map
        'Entry': 'map',
        'Guard Post': '',
        'Dining Hall': 'guild-member\'s_bag',
        'Social Room': 'money',
        'Planning Room': 'heist_plans',
        'Outside': '',
        'Treasure Room': 'treasure_chest',
        'Holding Cell': 'captured_ally',
        'Hidden Passageway': 'skeleton_key',
        'Main Hall': 'guild_secrets'
    }
}

# Randomly choosing a map to play
current_map_name = random.choice(list(maps))
rooms = maps[current_map_name]
print(current_map_name)
current_map_items = perception[current_map_name]

# Dictionary to store the loss condition room for each map
lose_con = {}

# Initializing player's inventory and user input
player_inventory = []
user_input = []


def main():
    global player_inventory, user_input
    current_room = 'Outside'  # Start the player outside the target location.

    # Welcome the player and explain the rules.
    print('Welcome to the Thieve\'s Guild. Today your target is the ' + current_map_name)
    print('To move, type \'go (direction)\' and to take an item, type \'get (item)\'')
    print('Get all the items you can, then go back outside without getting caught.')

    while True:  # Main game loop where the player can continue taking actions.

        # Check for lose condition
        if current_room == lose_con:
            print('You were caught! Game over.')
            break

        possible_directions = ', '.join(rooms[current_room].keys())  # Getting possible directions.

        # Display room info and available actions
        print(f'You are in the {current_room}. You can go: {possible_directions}')
        if current_map_items[current_room]:
            print(f'You see: {current_map_items[current_room]}')

        # Get user input for action
        user_input = input('What would you like to do? ').strip().lower()

        # Check if user wants to quit the game.
        if user_input == 'quit':
            print('You chose to exit the game. Goodbye!')
            break

        user_input = user_input.split()

        # Process user action: getting an item
        if user_input[0].lower() == 'get':
            item = user_input[1]
            if item == current_map_items[current_room]:
                player_inventory.append(item)
                print(f'You have added {item} to your inventory.')
            else:
                print(f'There is no item "{item}" in this room.')

        # Process user action: moving to a different room
        elif user_input[0].lower() == 'go':
            direction = user_input[1].capitalize()
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print(f'You cannot go {direction} from here.')
        else:
            print('Invalid action. Please use "go [direction]" or "get [item]".')

        # Check for the winning condition
        if current_room == 'Outside' and len(player_inventory) == len(current_map_items) - 1:
            print('Congratulations! You’ve escaped with all the items. You win!')
            break

# Call the main function to start the game
main()
