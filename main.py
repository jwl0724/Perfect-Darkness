from initialization import *
from mechanics import *
import random


def run_game():
    """
    Run the game
    """
    # set initial variables
    player_stats, monster_stats = (10, 1, 0), (50, 10, 10)
    player_coords, monster_coords = (2, 0, 0), (2, 2, 4)
    rows, height, column = 5, 3, 5

    # set constants
    VALID_ACTIONS = ('help', 'take', 'move', 'listen', 'flash')

    # intialize the game
    introduce_game()
    player = create_entity(player_stats, player_coords, 1, True)
    monster = create_entity(monster_stats, monster_coords, 2, False)
    building = make_board(rows, height, column)

    # start the game loop
    describe_location(player, building)
    while is_alive(player):
        # process input
        while True:
            player_input = helpers.enforced_input('Input: ', VALID_ACTIONS)
            match player_input:
                case 'help':
                    process_help()
                    continue
                case 'take':
                    if not process_take(player, building):
                        continue
                case 'move':
                    process_move(player, building)
                case 'listen':
                    process_listen(player, monster)
                case 'flash':
                    process_flash(player, monster)
            break

        print(player['X'], player['Y'], player['Z'])
        describe_location(player, building)


def main():
    run_game()


if __name__ == '__main__':
    main()
