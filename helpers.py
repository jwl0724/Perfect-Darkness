def is_between(number, lower_bound, upper_bound):
    if lower_bound <= number <= upper_bound:
        return True
    else:
        return False


def enforced_input(input_message, valid_input_list):
    player_input = input(input_message)
    while player_input not in valid_input_list:
        print('Invalid command, type help for a list of commands')
        player_input = input(input_message)

    return player_input
