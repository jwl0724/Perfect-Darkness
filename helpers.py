def is_between(number, lower_bound, upper_bound):
    if lower_bound <= number <= upper_bound:
        return True
    else:
        return False


def enforced_input(input_message, valid_input_list):
    player_input = input(input_message).strip().lower()
    while player_input not in valid_input_list:
        print('Invalid input, type help for a list of valid inputs')
        player_input = input(input_message)

    return player_input


def change_board_event(board, coordinate, new_event, description):
    board[coordinate]['Event'] = new_event
    board[coordinate]['Description'] = description


def out_of_bounds(entity, board, direction, speed=None):
    direction_key = {'n': 1, 's': -1, 'e': 1, 'w': -1, 'up': 1, 'down': -1}
    entity_spd = speed if speed else entity['SPD']
    board_row = list(board.keys())[-1][0]
    board_col = list(board.keys())[-1][2]
    board_height = list(board.keys())[-1][1]

    if direction == 'n' or direction == 's':
        new_position = entity['Z'] + direction_key[direction] * entity_spd
        if new_position > board_col or new_position < 0:
            return True

    if direction == 'e' or direction == 'w':
        new_position = entity['X'] + direction_key[direction] * entity_spd
        if new_position > board_row or new_position < 0:
            return True

    if direction == 'up' or direction == 'down':
        new_position = entity['Y'] + direction_key[direction] * entity_spd
        if new_position > board_height or new_position < 0:
            return True

    return False


def move(entity, direction, speed=None):
    entity_spd = speed if speed else entity['SPD']
    direction_key = {'n': 1, 's': -1, 'e': 1, 'w': -1, 'up': 1, 'down': -1}

    entity['X'] += entity_spd * direction_key[direction] if direction == 'e' or direction == 'w' else 0
    entity['Z'] += entity_spd * direction_key[direction] if direction == 'n' or direction == 's' else 0
    entity['Y'] += entity_spd * direction_key[direction] if direction == 'up' or direction == 'down' else 0


def is_alive(entity):
    if entity['HP'] == 0:
        return False
    else:
        return True
