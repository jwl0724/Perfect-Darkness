"""
Jonathan Liu
A01375621
"""
import pygame as pg
import os


def is_between(number: int or float, lower_bound: int or float, upper_bound: int or float) -> bool:
    """
    Determine if a number is between two bounds

    This function takes a real number and two real number bounds and determines if the number lies between the two
    bounds.

    :param number: A real number which is to be determined if it lies between the bounds
    :param lower_bound: A real number that represents the lower bounds of a range
    :param upper_bound: A real number that represents the upper bounds of a range
    :precondition: lower_bound must be less than upper_bound
    :precondition: All parameters must be either int or float types
    :postcondition: The number parameter is evaluated to see if it is between the two bounds
    :return: Returns True if number is between the bounds, False otherwise

    >>> is_between(1, 6, 9)
    False

    >>> is_between(1.5, 0, 6.9)
    True
    """
    return True if lower_bound <= number <= upper_bound else False


def change_board_event(board: dict, coordinate: tuple, new_event: str, description: str) -> None:
    """
    Update board event and change its description

    This function updates the event type at the inputted coordinate, and replaces it with the arguments passed into
    the function

    :param board: A dictionary that representing the playable area
    :param coordinate: A tuple that represents a set of coordinates on the board
    :param new_event: A string that represents a new event type to update the board with
    :param description: A string that represents a new description to be inserted at the coordinate
    :precondition: board must be a dictionary that represents the playable area, in the correct format
    :precondition: coordinate must be a tuple that exists within the playable area
    :precondition: new_event must be a string that corresponds to the possible event types within the board
    :postcondition: The board will be updated with a new event type and a new description at the specified coordinates

    >>> test_board = {(0, 0, 0): {'Event': 'Salvage', 'Description': 'Desc Here'}}
    >>> change_board_event(test_board, (0, 0, 0), 'None', 'New Desc')
    >>> print(test_board)
    {(0, 0, 0): {'Event': 'None', 'Description': 'New Desc'}}

    >>> test_board = {(6, 6, 9): {'Event': 'None', 'Description': 'Zoinks'}}
    >>> change_board_event(test_board, (6, 6, 9), 'Salvage', 'Jeepers')
    >>> print(test_board)
    {(6, 6, 9): {'Event': 'Salvage', 'Description': 'Jeepers'}}
    """
    board[coordinate]['Event'] = new_event
    board[coordinate]['Description'] = description


def out_of_bounds(entity: dict, board: dict, direction: pg.constants, speed: int = None) -> bool:
    """
    Check direction validity

    This function takes in a direction represented by a pygame constant for key presses, and determines if said
    direction causes the new coordinates to go out of bounds and returns True if it does.

    :param entity: A dictionary representing an entity in the game (player or monster)
    :param board: A dictionary representing the playable area
    :param direction: A pygame constant that represents a key press that determines which direction to move
    :param speed: An integer representing amount of units to move, defaults to None when no argument is passed
    :precondition: entity and board must be dictionaries representing an entity and the playable area respectively
    :precondition: direction must be a pygame constant for the keys W, A, S, D, up arrow, down arrow
    :postcondition: The validity of the movement is evaluated and returned
    :return: A boolean True if the input direction goes out of bounds, False otherwise

    >>> test_board = {(0, 0, 0): {'Event': 'None', 'Description':  'Wow'}, (1, 0, 0): {'Event': 'None', 'Description': 'Cool'}}
    >>> sample_player = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
    >>> out_of_bounds(sample_player, test_board, pg.K_d)
    False

    >>> test_board = {(0, 0, 0): {'Event': 'None', 'Description':  'Wow'}, (1, 0, 0): {'Event': 'None', 'Description': 'Cool'}}
    >>> sample_player = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
    >>> out_of_bounds(sample_player, test_board, pg.K_a)
    True
    """
    direction_key = {pg.K_w: 1, pg.K_s: -1, pg.K_d: 1, pg.K_a: -1, pg.K_UP: 1, pg.K_DOWN: -1}
    # set entity speed to custom value if passed into the function
    entity_spd = speed if speed else entity['SPD']
    # get the board row, col, and height
    board_row = list(board.keys())[-1][0]
    board_col = list(board.keys())[-1][2]
    board_height = list(board.keys())[-1][1]

    # change Z coordinate if W or S was pressed
    if direction == pg.K_w or direction == pg.K_s:
        new_position = entity['Z'] + direction_key[direction] * entity_spd
        if new_position > board_col or new_position < 0:
            return True

    # change X coordinate if D or A was pressed
    elif direction == pg.K_d or direction == pg.K_a:
        new_position = entity['X'] + direction_key[direction] * entity_spd
        if new_position > board_row or new_position < 0:
            return True

    # change Y coordinate if up arrow or down arrow was pressed
    elif direction == pg.K_UP or direction == pg.K_DOWN:
        new_position = entity['Y'] + direction_key[direction] * entity_spd
        if new_position > board_height or new_position < 0:
            return True

    # cleared the if elif blocks, therefore it is in bounds, return False
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
