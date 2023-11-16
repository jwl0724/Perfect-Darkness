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
            Take - Spend a turn to take an item, with a 5% chance of failing
            Move - Spend a turn to move in a direction
            Listen - Spend a turn to focus listening to estimate where the monster is
            Flash - Spend a turn to get exact location of the monster, also alerts the monster to your location
            """)
        elif player_input in valid_action:
            return player_input


def process_take(player, board):
    """
    Process taking items from board

    :param player: A dictionary that represents a player character
    :param board: A dictionary representing the playable area, populated with descriptions
    :precondition: player and board must be valid representations of their respective objects in the correct format
    :postcondition: After taking an item, the player's stats will increase based on what was taken
    :poscondition: The board at the coordinates will be changed to none-type event
    :return: A boolean value, returns True if an item was taken, False otherwise
    """
    player_coords = (player['X'], player['Y'], player['Z'])
    board_event = board[player_coords]['Event']
    if board_event != 'Salvage':
        return False

    random_number = random.randint(1, 20)
    if random_number == 4:
        print('You tried to grab the item, but fumbled in the darkness. The item is now lost into void of darkness')

    # possible items: lid, bottle, knife, scissor, gun, armor
    atk_booster = ['bottle', 'knife', 'gun', 'scissor']
    def_booster = ['lid', 'armor']
    all_items = atk_booster + def_booster

    for item in all_items:
        if item in board[player_coords]['Description']:
            print(f'You managed to grab the {item} without issue.')
            player['ATK'] += 1 if item in atk_booster else 0
            player['DEF'] += 1 if item in def_booster else 0

            feedback_message = f'You now have increased offensive power with the {item}.' if item in atk_booster else\
                f'You now take less damage thanks to your {item}'
            print(feedback_message)
            new_description = 'An empty void of darkness, it used to contain things, but you looted it.'
            helpers.change_board_event(board, player_coords, 'None', new_description)

    return True


def process_move(player, board):
    pass


def process_flash(monster):
    pass


def process_listen(player, monster):
    print('You stop everything, and focus intensely on listening to your surroundings.')

    # process monster on different floor as player
    if player['Y'] > monster['Y']:
        print('You pick up on some subtle shuffling on the floors below, the monster must be there...')
        return
    elif player['Y'] < monster['Y']:
        print('You pick up some faint movement on the floors above, the monster must be there...')
        return

    monster_location_description = 'You pick up some faint sounds coming from '

    if player['Z'] < monster['Z']:
        monster_location_description += 'north'
    elif player['Z'] > monster['Z']:
        monster_location_description += 'south'
    if player['X'] < monster['X']:
        monster_location_description += 'west'
    elif player['X'] > monster['X']:
        monster_location_description += 'east'

    monster_location_description += ' of you. Best to avoid that place for now...'

    print(monster_location_description)

def get_direction():
    valid_direction = ('n', 's', 'e', 'w', 'up', 'down')
