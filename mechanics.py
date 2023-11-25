import random
import helpers


def is_alive(entity):
    if entity['HP'] == 0:
        return False
    else:
        return True


def describe_location(player, board):
    description = board[(player['X'], player['Y'], player['Z'])]['Description']
    print(description)
