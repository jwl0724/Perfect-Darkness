import random
import helpers


def move_monster(monster, board):
    available_directions = ('n', 's', 'e', 'w', 'up', 'down')
    monster_not_moved = True

    while monster_not_moved:
        move_unit = random.randint(1, monster['SPD'])
        direction = available_directions[random.randint(0, 5)]
        if helpers.out_of_bounds(monster, board, direction, move_unit):
            continue

        helpers.move(monster, direction, move_unit)
        monster_not_moved = False


def chase_player(player, monster):
    if player['X'] != monster['X']:
        direction = 'e' if player['X'] > monster['X'] else 'w'
        difference = abs(player['X'] - monster['X'])
        move_unit = monster['SPD'] if difference > 2 else difference
        helpers.move(monster, direction, move_unit)

    elif player['Y'] != monster['Y']:
        direction = 'up' if player['Y'] > monster['Y'] else 'down'
        difference = abs(player['Y'] - monster['Y'])
        move_unit = monster['SPD'] if difference > 2 else difference
        helpers.move(monster, direction, move_unit)

    elif player['Z'] != monster['Z']:
        direction = 'n' if player['Z'] > monster['Z'] else 's'
        difference = abs(player['Z'] - monster['Z'])
        move_unit = monster['SPD'] if difference > 2 else difference
        helpers.move(monster, direction, move_unit)

    monster['Alert Counter'] -= 1
    if monster['Alert Counter'] == 0:
        monster['Alerted'] = False
