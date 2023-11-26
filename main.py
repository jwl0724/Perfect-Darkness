import initialization as init
import mechanics as mech
import monster as mon
import helpers
import input as ipt


def run_game():
    """
    Run the game
    """
    # set initial variables
    player_stats, monster_stats = (10, 1, 0), (50, 10, 10)
    player_coords, monster_coords = (2, 0, 0), (2, 2, 4)
    rows, height, column = 5, 3, 5

    # set constants
    VALID_ACTIONS = ('help', 'take', 'move', 'listen', 'flash', 'save', 'load')

    # initialize the game
    init.introduce_game()
    player = init.create_entity(player_stats, player_coords, 1, True)
    monster = init.create_entity(monster_stats, monster_coords, 2, False)
    building = init.make_board(rows, height, column)

    # start the game loop
    while mech.is_alive(player) and mech.is_alive(monster):

        # different description if monster on top of player
        if (monster['X'], monster['Y'], monster['Z']) == (player['X'], player['Y'], player['Z']):
            print('The creature is right behind you...')
        else:
            mech.describe_location(player, building)

        # determine if monster chasing player
        if monster['Alerted']:
            mon.chase_player(player, monster)
        else:
            mon.move_monster(monster, building)

        # process input
        while mech.is_alive(player):
            player_input = helpers.enforced_input('Input: ', VALID_ACTIONS)
            match player_input:
                case 'help':
                    ipt.process_help()
                    continue
                case 'take':
                    if not ipt.process_take(player, building):
                        continue
                case 'move':
                    ipt.process_move(player, building)
                case 'listen':
                    ipt.process_listen(player, monster)
                case 'flash':
                    ipt.process_flash(player, monster)
                case 'save':
                    ipt.process_save(player, monster, building)
                    decision = helpers.enforced_input('Quit Now? (Y/N): ', ['y', 'n'])
                    if decision == 'y':
                        print('Quitting now...')
                        return
                    else:
                        print('Resuming game...')
                        continue
                case 'load':
                    save_state = ipt.process_load()
                    if save_state:
                        print('Now loading...')
                    else:
                        print('Error, no saves found...')
                    continue

            break

        # start fight if coordinates overlap
        if (monster['X'], monster['Y'], monster['Z']) == (player['X'], player['Y'], player['Z']):
            mech.fight(player, monster)
            print('Fight occurred')

        print(f'Player Coords = ({player["X"]}, {player["Y"]}, {player["Z"]})')
        print(f'Monster Coords = ({monster["X"]}, {monster["Y"]}, {monster["Z"]})')

    if mech.is_alive(player):
        print('You somehow managed to defeat the creature, unfortunately the foundation has no intention of letting you go as you have seen too much. You have only staved off your execution for just a tiny bit...')
    elif mech.is_alive(monster):
        print('You tried defy your fate and survive, unfortunately it was just too much for you to handle.')


def main():
    run_game()


if __name__ == '__main__':
    main()
