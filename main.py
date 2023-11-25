import initialization as init
import mechanics as mech
import monster as mon
import helpers
import input


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

    # initialize the game
    init.introduce_game()
    player = init.create_entity(player_stats, player_coords, 1, True)
    monster = init.create_entity(monster_stats, monster_coords, 2, False)
    building = init.make_board(rows, height, column)

    # start the game loop
    mech.describe_location(player, building)
    while mech.is_alive(player):
        # process input
        while True:
            player_input = helpers.enforced_input('Input: ', VALID_ACTIONS)
            match player_input:
                case 'help':
                    input.process_help()
                    continue
                case 'take':
                    if not input.process_take(player, building):
                        continue
                case 'move':
                    input.process_move(player, building)
                case 'listen':
                    input.process_listen(player, monster)
                case 'flash':
                    input.process_flash(player, monster)
            break

        if (monster['X'], monster['Y'], monster['Z']) == (player['X'], player['Y'], player['Z']):
            mech.fight(player, monster)

        if not mech.is_alive(monster):
            print('You have slain the decrepit creature.')
            break
        mon.move_monster(monster, building)

        if (monster['X'], monster['Y'], monster['Z']) == (player['X'], player['Y'], player['Z']):
            mech.fight(player, monster)

        print(player['X'], player['Y'], player['Z'])
        mech.describe_location(player, building)


def main():
    run_game()


if __name__ == '__main__':
    main()
