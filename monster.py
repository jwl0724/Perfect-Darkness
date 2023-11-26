import random
import helpers


def move_monster(monster, board):
    direction_key = {1: 'n', 2: 's', 3: 'e', 4: 'w', 5: 'up', 6: 'down'}
    monster_not_moved = True

    while monster_not_moved:
        move_unit = random.randint(1, monster['SPD'])
        direction = direction_key[random.randint(1,6)]
        if helpers.out_of_bounds(monster, board, direction, move_unit):
            continue

        helpers.move(monster, direction, move_unit)
        monster_not_moved = False


def chase_player(player, monster):
    if player['X'] != monster['X']:
        direction = 'e' if player['X'] > monster['X'] else 'w'
        difference = player['X'] - monster['X']
        move_unit = monster['SPD'] if difference > 2 else difference
        helpers.move(monster, direction, move_unit)

    elif player['Y'] != monster['Y']:
        direction = 'up' if player['Y'] > monster['Y'] else 'down'
        difference = player['Y'] - monster['Y']
        move_unit = monster['SPD'] if difference > 2 else difference
        helpers.move(monster, direction, move_unit)

    elif player['Z'] != monster['Z']:
        direction = 'n' if player['Z'] > monster['Z'] else 's'
        difference = player['Z'] - monster['Z']
        move_unit = monster['SPD'] if difference > 2 else difference
        helpers.move(monster, direction, move_unit)

    monster['Alert Counter'] -= 1
    if monster['Alert Counter'] == 0:
        monster['Alerted'] = False
