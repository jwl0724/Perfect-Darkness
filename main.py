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
            player_input = get_action_input()

            if player_input == 'take':
                if process_take(player, building):
                    break

            elif player_input == 'move':
                process_move()

            elif player_input == 'listen':
                process_listen()

            elif player_input == 'flash':
                process_flash()


def main():
    run_game()


if __name__ == '__main__':
    main()
