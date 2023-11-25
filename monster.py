import random
import helpers


def move_monster(monster, board):
    direction_key = {1: 'n', 2: 's', 3: 'e', 4: 'w', 5: 'up', 6: 'down'}
    monster_not_moved = True

    while monster_not_moved:
        direction = direction_key[random.randint(1,6)]
        if helpers.out_of_bounds(monster, board, direction):
            continue

        helpers.move(monster, direction)
