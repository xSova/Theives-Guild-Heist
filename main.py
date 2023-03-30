# Bryce Schultz
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}


def move():
    current_room = 'Great Hall'  # default room

    while True:
        possible_directions = ', '.join(rooms[current_room].keys())
        print('You are in the', current_room + '.')
        user_input = input(f'Where would you like to go? ({possible_directions}): ')  # FIXME make option tree for actions (move, observe, take)
        if user_input == "Quit":
            break
        while user_input not in rooms[current_room].keys():
            print('Error, direction invalid.')
            user_input = input(f'Choose from ({possible_directions}): ')
        current_room = rooms[current_room][user_input]
    print('Thanks for playing!')


move()
