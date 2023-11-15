from initialization import *
from mechanics import *
import random


def run_game():
    """
    Run the game
    """
    player_stats, monster_stats = (10, 1, 0), (50, 10, 10)
    player_coords, monster_coords = (2, 0, 0), (2, 2, 4)
    rows, height, column = 5, 3, 5

    introduce_game()

    player = create_entity(player_stats, player_coords, 1, True)
    monster = create_entity(monster_stats, monster_coords, 2, True)
    building = make_board(rows, height, column)
    print(player, monster, building)


def main():
    run_game()


if __name__ == '__main__':
    main()
