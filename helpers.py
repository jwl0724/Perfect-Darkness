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


def out_of_bounds(entity, board, direction):
    direction_key = {'n': 1, 's': -1, 'e': -1, 'w': 1}
    board_row = list(board.keys())[-1][0]
    board_col = list(board.keys())[-1][2]

    if direction == 'n' or direction == 's':
        if entity['Z'] + direction_key[direction] > board_col or entity['Z'] + direction_key[direction] < 0:
            return True

    if direction == 'e' or direction == 'w':
        if entity['X'] + direction_key[direction] > board_row or entity['X'] + direction_key[direction] < 0:
            return True

    return False
