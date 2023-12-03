import pygame as pg
import os


def is_between(number, lower_bound, upper_bound):
    if lower_bound <= number <= upper_bound:
        return True
    else:
        return False


def enforced_input(input_message, valid_input_list, help_msg=True):
    player_input = input(input_message).strip().lower()
    while player_input not in valid_input_list:
        print('Invalid input, type help for a list of valid inputs') if help_msg else print('Invalid input.')
        player_input = input(input_message).strip().lower()

    return player_input


def change_board_event(board, coordinate, new_event, description):
    board[coordinate]['Event'] = new_event
    board[coordinate]['Description'] = description


def out_of_bounds(entity, board, direction, speed=None):
    direction_key = {pg.K_w: 1, pg.K_s: -1, pg.K_d: 1, pg.K_a: -1, pg.K_UP: 1, pg.K_DOWN: -1}
    entity_spd = speed if speed else entity['SPD']
    board_row = list(board.keys())[-1][0]
    board_col = list(board.keys())[-1][2]
    board_height = list(board.keys())[-1][1]

    if direction == pg.K_w or direction == pg.K_s:
        new_position = entity['Z'] + direction_key[direction] * entity_spd
        if new_position > board_col or new_position < 0:
            return True

    if direction == pg.K_d or direction == pg.K_a:
        new_position = entity['X'] + direction_key[direction] * entity_spd
        if new_position > board_row or new_position < 0:
            return True

    if direction == pg.K_UP or direction == pg.K_DOWN:
        new_position = entity['Y'] + direction_key[direction] * entity_spd
        if new_position > board_height or new_position < 0:
            return True

    return False


def move(entity, key_pressed, speed=None):
    entity_spd = speed if speed else entity['SPD']
    direction_key = {pg.K_w: 1, pg.K_s: -1, pg.K_d: 1, pg.K_a: -1, pg.K_UP: 1, pg.K_DOWN: -1}

    entity['X'] += entity_spd * direction_key[key_pressed] if key_pressed == pg.K_a or key_pressed == pg.K_d else 0
    entity['Z'] += entity_spd * direction_key[key_pressed] if key_pressed == pg.K_s or key_pressed == pg.K_w else 0
    entity['Y'] += entity_spd * direction_key[key_pressed] if key_pressed == pg.K_UP or key_pressed == pg.K_DOWN else 0


def is_alive(entity):
    if entity['HP'] <= 0:
        return False
    else:
        return True


def describe_location(player, board):
    description = board[(player['X'], player['Y'], player['Z'])]['Description']
    return description


def convert_dictionary(board):
    converted_dictionary = {}

    if type(tuple(board.keys())[0]) == tuple:
        for key, value in board.items():
            converted_dictionary[str(key)] = value
    else:
        for key, value in board.items():
            converted_dictionary[eval(key)] = value

    return converted_dictionary


def get_saves_list():
    file_num = 1
    file_path = os.path.join(os.path.dirname(__file__), 'saves')

    if not os.path.exists(file_path) or not len(os.listdir(file_path)):
        return None

    existing_save_numbers = []
    while len(existing_save_numbers) != len(os.listdir(file_path)):
        if os.path.exists(os.path.join(file_path, f'save-{file_num}.json')):
            existing_save_numbers.append(str(file_num))
        file_num += 1

    return existing_save_numbers
