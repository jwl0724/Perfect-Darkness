import random
import helpers
import pygame as pg


def move_monster(monster: dict, board: dict) -> None:
    """
    Move the monster

    This function randomly generates a direction and movement unit for the monster to move towards, and if it results in
    the monster going out of bounds, a new direction and unit is generated until it stays in bound

    :param monster: A dictionary that represents a monster
    :param board: A dictionary that represents the playable area
    :precondition: monster and board must accurately reflect what they represent and is correctly formatted
    :postcondition: The monster coordinates are changed
    """
    available_keys = (pg.K_w, pg.K_s, pg.K_d, pg.K_a, pg.K_UP, pg.K_DOWN)
    monster_not_moved = True

    while monster_not_moved:
        move_unit = random.randint(1, monster['SPD'])
        direction = available_keys[random.randint(0, 5)]
        if helpers.out_of_bounds(monster, board, direction, move_unit):
            continue

        helpers.move(monster, direction, move_unit)
        monster_not_moved = False


def chase_player(player: dict, monster: dict) -> None:
    """
    Move monster towards player

    This function will move the monster towards the coordinates of which the player resides at when called

    :param player: A dictionary that represents the player that has the player's coordinates
    :param monster: A dictionary that represents the monster that has the monster's coordinates
    :precondition: player and monster must be dictionaries that represent the player and monster respectively
    :postcondition: The monster coordinates will be moved towards the player's coordinates until they overlap

    >>> sample_player = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
    >>> sample_monster = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 2, 'Y': 0, 'Z': 0, 'SPD': 2, 'Alerted': True, 'Alert Counter': 20}
    >>> chase_player(sample_player, sample_monster)
    >>> sample_monster
    {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 2, 'Alerted': True, 'Alert Counter': 19}

    >>> sample_player = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
    >>> sample_monster = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 1, 'SPD': 2, 'Alerted': True, 'Alert Counter': 1}
    >>> chase_player(sample_player, sample_monster)
    >>> sample_monster
    {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 2, 'Alerted': False, 'Alert Counter': 0}
    """
    if player['X'] != monster['X']:
        direction = pg.K_d if player['X'] > monster['X'] else pg.K_a
        difference = abs(player['X'] - monster['X'])
        move_unit = monster['SPD'] if difference > 2 else difference
        helpers.move(monster, direction, move_unit)

    elif player['Y'] != monster['Y']:
        direction = pg.K_UP if player['Y'] > monster['Y'] else pg.K_DOWN
        difference = abs(player['Y'] - monster['Y'])
        move_unit = monster['SPD'] if difference > 2 else difference
        helpers.move(monster, direction, move_unit)

    elif player['Z'] != monster['Z']:
        direction = pg.K_w if player['Z'] > monster['Z'] else pg.K_s
        difference = abs(player['Z'] - monster['Z'])
        move_unit = monster['SPD'] if difference > 2 else difference
        helpers.move(monster, direction, move_unit)

    monster['Alert Counter'] -= 1
    if monster['Alert Counter'] == 0:
        monster['Alerted'] = False
