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
