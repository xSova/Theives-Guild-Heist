import random

# Bryce Schultz
maps = {
    'Bank': {
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
current_map_name = random.choice(list(maps))
rooms = maps[current_map_name]
print(current_map_name)
current_map_items = perception[current_map_name]
lose_con = ['Guard Post', 'Staff Chambers', 'Security Desk']
player_inventory = []
user_input = []


def main():
    global player_inventory, user_input
    current_room = 'Outside'  # default room
    print('Welcome to the Thieve\'s Guild. Today your target is the ' + current_map_name)
    print('To move, type \'go (direction)\' and to take an item, type \'get (item)\'')
    print('Get all the items you can, then go back outside without getting caught.')

    while True:
        possible_directions = ', '.join(rooms[current_room].keys())

        if current_room == 'Outside':
            if (len(player_inventory)) == (len(current_map_items) - 2):
                print('You\'ve escaped with all the items! Good work!')
                break
            user_input = input(f'You are outside. Where would you like to go? {possible_directions}:\n').split()
            current_room = rooms[current_room][user_input[1]]
            if user_input[0] == "Quit":
                break
            if user_input[1] not in possible_directions:
                print('Direction invalid.')
                user_input = input(f'Choose from go/get ({possible_directions})(item):\n').split()
        elif current_room not in lose_con:
            if user_input[0] in ['Quit', 'quit']:
                break
            print('You are in the', current_room + f'. You see: {current_map_items[current_room]}')
            user_input = input(
                f'What would you like to do? (You can go: {possible_directions} or get(item):\n').split()
            if user_input[0] == "Quit":
                break
            if user_input[0] in ['get', 'Get']:
                if user_input[1] != current_map_items[current_room]:
                    print('Error can not get that item.')
                    user_input = input(
                        f'What would you like to do? (You can go: {possible_directions} or get(item):\n').split()
                elif user_input[1] in player_inventory:
                    print(f'You already have {user_input[1]} in your inventory: {player_inventory}.')
                    user_input = input(
                        f'What would you like to do? (You can go: {possible_directions} or get(item):\n').split()
                else:
                    player_inventory.append(user_input[1])
                    print(f'{user_input[1]} successfully added to inventory.')
                    print(f'Inventory: {player_inventory}')
                    user_input = input(
                        f'What would you like to do? (You can go: {possible_directions} or get(item):\n').split()
            if user_input[0] in ['go', 'Go']:
                if user_input[1] not in possible_directions:
                    print('Direction invalid.')
                    user_input = input(f'Choose from go/get ({possible_directions})(item):\n').split()
                current_room = rooms[current_room][user_input[1]]
            if user_input[0] not in ['go', 'get', 'Go', 'Get']:
                print('Error, command invalid.')
                user_input = input(f'Choose from go/get ({possible_directions})(item):\n').split()
            if user_input[1] not in possible_directions:
                print('Direction invalid.')
                user_input = input(f'Choose from go/get ({possible_directions})(item):\n').split()
        else:
            print('You were caught! Game over.')
            break
    print('Thanks for playing!')


main()
