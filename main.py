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
    while mech.is_alive(player) and mech.is_alive(monster):
        mech.describe_location(player, building)

        # start fight if coordinates overlap
        if (monster['X'], monster['Y'], monster['Z']) == (player['X'], player['Y'], player['Z']):
            mech.fight(player, monster)

        # process input
        while mech.is_alive(player):
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
                case 'save':
                    input.process_save(player, monster, building)
                    decision = helpers.enforced_input('Quit Now? (Y/N)', ['y', 'n']) == 'y'
                    if decision == 'y':
                        print('Quitting now...')
                        return
                    else:
                        print('Resuming game...')
                        continue
            break

        mon.move_monster(monster, building)

        print(player['X'], player['Y'], player['Z'])

    if mech.is_alive(player):
        print('You somehow managed to defeat the creature, unfortunately the foundation has no intention of letting you go as you have seen too much. You have only staved off your execution for just a tiny bit...')
    elif mech.is_alive(monster):
        print('You tried defy your fate and survive, unfortunately it was just too much for you to handle.')


def main():
    run_game()


if __name__ == '__main__':
    main()
