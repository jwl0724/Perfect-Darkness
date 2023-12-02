import initialization as init
import mechanics as mech
import monster as mon
import helpers
import input as ipt
import pygame as pg
import pygame_helpers as pg_help
import constants as con
import sys 


def run_game():
    # set initial variables
    player_stats, monster_stats = (20, 1, 0), (100, 10, 10)
    player_coords, monster_coords = (4, 0, 0), (2, 2, 4)
    rows, height, column = 10, 3, 10
    game_running = True
    
    # set valid key for parts of the game
    overworld_inputs = [pg.K_w, pg.K_a, pg.K_s, pg.K_d, pg.K_UP, pg.K_DOWN, pg.K_l, pg.K_ESCAPE, pg.K_f, pg.K_RETURN, pg.K_h]
    fight_inputs = [pg.K_1, pg.K_2, pg.K_3, pg.K_4]
    pause_menu_inputs = [pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5]

    # initialize the game
    player = init.create_entity(player_stats, player_coords, 1, True)
    monster = init.create_entity(monster_stats, monster_coords, 2, False)
    building = init.make_board(rows, height, column)

    # initialize pygame resources
    pg.init()

    # create screen
    screen = pg.display.set_mode((1080, 720))
    pg.display.set_caption('Perfect Darkness')

    # Draw the GUI and set up story
    screen.fill((0, 0, 0))
    pg_help.draw_windows(screen)
    # pg_help.play_sound(con.start_sound)
    pg_help.draw_image(screen, con.default_img)
    pg_help.draw_one_line_text(screen, con.intro_msg_list)

    while game_running and helpers.is_alive(player) and helpers.is_alive(monster):
        
        pg_help.draw_image(screen, con.default_img)

        # different description if monster on top of player
        if (monster['X'], monster['Y'], monster['Z']) == (player['X'], player['Y'], player['Z']):
            pg_help.draw_one_line_text(screen, 'The creature is right behind you...', wait=False)
        else:
            pg_help.draw_one_line_text(screen, mech.describe_location(player, building), wait=False)

        # move the monster depending on its state
        if monster['Alerted']:
            mon.chase_player(player, monster)
        else:
            mon.move_monster(monster, building)

        while True:
            key_pressed = pg_help.wait_for_input(overworld_inputs)
            match(key_pressed):
                case pg.K_h:
                    pg_help.draw_multi_line_text(screen, con.overworld_help_msg_list, size=33, wait=False)
                case pg.K_RETURN:
                    if ipt.process_take(screen, player, building):
                        break
                case pg.K_l:
                    ipt.process_listen(screen, player, monster)
                    break
                case pg.K_f:
                    ipt.process_flash(screen, player, monster, building)
                    break
                case pg.K_ESCAPE:
                    pg_help.draw_multi_line_text(screen, con.pause_menu_list, size=28, wait=False)
                    selected = pg_help.wait_for_input(pause_menu_inputs)

                    if selected == pg.K_1:
                        ipt.process_save(player, monster, building)
                        pg_help.draw_one_line_text(screen, 'Game Successfully Saved...')

                    elif selected == pg.K_2:
                        save_data = ipt.process_load(screen)
                        if save_data == 'canceled':
                            pg_help.draw_one_line_text(screen, 'Returning To Game...')
                        elif save_data:
                            player = save_data[0]
                            monster = save_data[1]
                            building = helpers.convert_dictionary(save_data[2])
                            pg_help.draw_one_line_text(screen, 'Save File Loaded...')
                        else:
                            pg_help.draw_one_line_text(screen, 'No Saves Found...')

                    elif selected == pg.K_3:
                        outcome = ipt.process_delete(screen)
                        if outcome == 'canceled':
                            pg_help.draw_one_line_text(screen, 'Delete Canceled, Returning to Game...')
                        elif outcome:
                            pg_help.draw_one_line_text(screen, 'Save File Deleted...')
                        else:
                            pg_help.draw_one_line_text(screen, 'No Saves Found...')

                    elif selected == pg.K_4:
                        pg_help.draw_one_line_text(screen, 'Resuming...')
                        
                    elif selected == pg.K_5:
                        pg.quit()
                        sys.exit()

                    pg_help.draw_one_line_text(screen, mech.describe_location(player, building), wait=False)
                    continue 
                case _:
                    if ipt.process_move(screen, player, monster, building, key_pressed):
                        break
                    
        # start fight if coordinates overlap
        if (monster['X'], monster['Y'], monster['Z']) == (player['X'], player['Y'], player['Z']):
            pg_help.draw_one_line_text(screen, 'The creature emerges from the darkness...')
            pg_help.draw_image(screen, con.monster_img)
            # pg_help.play_sound(con.alert_sound)
            mech.fight(screen, fight_inputs, player, monster)
        
    if helpers.is_alive(player):
        pg_help.draw_one_line_text(screen, con.winning_end_msg_list)
    elif helpers.is_alive(monster):
        pg_help.draw_one_line_text(screen, con.losing_end_msg_list)

    pg.quit()


def main():
    run_game()


if __name__ == '__main__':
    main()