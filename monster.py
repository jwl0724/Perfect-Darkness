import random
import helpers
import pygame as pg


def move_monster(monster, board):
    available_keys = (pg.K_w, pg.K_s, pg.K_d, pg.K_a, pg.K_UP, pg.K_DOWN)
    monster_not_moved = True

    while monster_not_moved:
        move_unit = random.randint(1, monster['SPD'])
        direction = available_keys[random.randint(0, 5)]
        if helpers.out_of_bounds(monster, board, direction, move_unit):
            continue

        helpers.move(monster, direction, move_unit)
        monster_not_moved = False


def chase_player(player, monster):
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
