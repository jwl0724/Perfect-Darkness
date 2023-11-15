import random
import helpers


def is_alive(entity):
    if entity['HP'] == 0:
        return False
    else:
        return True


def describe_location(player, board):
    description = board[(player['X'], player['Y'], player['Z'])]
    print(description)


def get_action_input():
    valid_action = ('help', 'take', 'move', 'listen', 'flash')

    print('What would you like to do? (type help for a list of commands)')
    # process action
    while True:
        player_input = helpers.enforced_input('Input: ', valid_action)
        if player_input == 'help':
            print("""
            Take - Spend a turn to take an item
            Move - Spend a turn to move in a direction
            Listen - Spend a turn to focus listening to estimate where the monster is
            Flash - Spend a turn to get exact location of the monster, also alerts the monster to your location
            """)
        elif player_input in valid_action:
            return player_input


def get_direction():
    valid_direction = ('n', 's', 'e', 'w', 'up', 'down')
