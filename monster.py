import random
import helpers


def move_monster(monster, board):
    direction_key = {1: 'n', 2: 's', 3: 'e', 4: 'w', 5: 'up', 6: 'down'}
    direction_value = {'n': 1, 's': -1, 'e': 1, 'w': -1, 'up': 1, 'down': -1}
    monster_not_moved = True

    while monster_not_moved:
        direction = direction_key[random.randint(1,6)]
        if helpers.out_of_bounds(monster, board, direction):
            continue

        monster['X'] += direction_value if direction == 'w' or direction == 'e' else 0
        monster['Y'] += direction_value if direction == 'up' or direction == 'down' else 0
        monster['Z'] += direction_value if direction == 'n' or direction == 's' else 0
        monster_not_moved = False
