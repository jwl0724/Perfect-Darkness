"""
Jonathan Liu
A01375621
"""
import initialization as init
import fight
import monster as mon
import helpers
import input as ipt
import pygame as pg
import pygame_helpers as pg_help
import constants as con
import sys 


def run_game() -> None:
    """
    Run the overarching game
    """
    # set initial variables
    player_stats, monster_stats = (20, 1, 0), (200, 15, 20)
    player_coords, monster_coords = (4, 0, 0), (2, 2, 4)
    rows, height, column = 10, 3, 10
    
    # set valid key for parts of the game
    overworld_inputs = (pg.K_w, pg.K_a, pg.K_s, pg.K_d, pg.K_UP, pg.K_DOWN,
                        pg.K_l, pg.K_ESCAPE, pg.K_f, pg.K_RETURN, pg.K_h)
    fight_inputs = (pg.K_1, pg.K_2, pg.K_3, pg.K_4)
    pause_menu_inputs = (pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5)

    # initialize the game
    player = init.create_entity(player_stats, player_coords, 1)
    monster = init.create_entity(monster_stats, monster_coords, 2, Alerted=False, Alert_Counter=0)
    building = init.make_board(rows, height, column)

    # initialize pygame resources
    pg.init()

    # create screen
    screen = pg.display.set_mode((1080, 720))
    pg.display.set_caption('Perfect Darkness')
    icon = pg.image.load(con.icon_img)
    pg.display.set_icon(icon)

    # Draw the GUI and set up story
    screen.fill((0, 0, 0))
    pg_help.draw_windows(screen)
    pg_help.play_sound(con.start_sound)
    pg_help.draw_image(screen, con.default_img)
    pg_help.draw_one_line_text(screen, con.intro_msg_list)

    while helpers.is_alive(player) and helpers.is_alive(monster):
        # play sound ambience sound and draw the default darkness image
        pg_help.play_random_ambience()
        pg_help.draw_image(screen, con.default_img)

        # show different description if monster on top of player
        if (monster['X'], monster['Y'], monster['Z']) == (player['X'], player['Y'], player['Z']):
            pg_help.draw_one_line_text(screen, 'The creature is right behind you...', wait=False)
        else:
            pg_help.draw_one_line_text(screen, helpers.describe_location(player, building), wait=False)

        # move the monster depending on its state
        if monster['Alerted']:
            mon.chase_player(player, monster)
        else:
            mon.move_monster(monster, building)

        # process key presses
        while True:
            key_pressed = pg_help.wait_for_input(overworld_inputs)
            match key_pressed:
                # when the H is pressed, show a help text
                case pg.K_h:
                    pg_help.draw_multi_line_text(screen, con.overworld_help_msg_list, size=33, wait=False)

                # when enter is pressed, take an item if it exists
                case pg.K_RETURN:
                    if ipt.process_take(screen, player, building):
                        break

                # when L is pressed, spend a turn to show where monster is through text
                case pg.K_l:
                    ipt.process_listen(screen, player, monster)
                    break

                # when F is pressed, spend a turn to print out a map that shows everything on current floor
                case pg.K_f:
                    ipt.process_flash(screen, player, monster, building)
                    break

                # when ESC is pressed, open the pause menu and do operations relating to files
                case pg.K_ESCAPE:
                    pg_help.draw_multi_line_text(screen, con.pause_menu_list, size=28, wait=False)
                    selected = pg_help.wait_for_input(pause_menu_inputs)

                    # save current session
                    if selected == pg.K_1:
                        ipt.process_save(player, monster, building)
                        pg_help.draw_one_line_text(screen, 'Game Successfully Saved...')

                    # load a save file if it exists
                    elif selected == pg.K_2:
                        save_data = ipt.process_load(screen)
                        # do nothing when escape is pressed when selecting a save
                        if save_data == -1:
                            pg_help.draw_one_line_text(screen, 'Returning To Game...')
                        # load the save data
                        elif save_data:
                            player = save_data[0]
                            monster = save_data[1]
                            building = helpers.convert_dictionary(save_data[2])
                            pg_help.draw_one_line_text(screen, 'Save File Loaded...')
                        # show message that no saves were found
                        else:
                            pg_help.draw_one_line_text(screen, 'No Saves Found...')

                    # delete a save file, if any exists
                    elif selected == pg.K_3:
                        outcome = ipt.process_delete(screen)
                        # do nothing when escape is pressed when selecting a save to delete
                        if outcome == -1:
                            pg_help.draw_one_line_text(screen, 'Delete Canceled, Returning to Game...')
                        # print a message saying that the save file has been deleted
                        elif outcome:
                            pg_help.draw_one_line_text(screen, 'Save File Deleted...')
                        # print a message saying that no save files were found
                        else:
                            pg_help.draw_one_line_text(screen, 'No Saves Found...')

                    # exit the pause menu and continue game
                    elif selected == pg.K_4:
                        pg_help.draw_one_line_text(screen, 'Resuming...')

                    # quit the game
                    elif selected == pg.K_5:
                        pg.quit()
                        sys.exit()

                    # describe the location again
                    pg_help.draw_one_line_text(screen, helpers.describe_location(player, building), wait=False)
                    continue
                # for movement in cardinal directions, up and down
                case _:
                    # if the move was valid, get out of the wait for input loop
                    if ipt.process_move(screen, player, monster, building, key_pressed):
                        break
                    
        # start fight if coordinates overlap
        if (monster['X'], monster['Y'], monster['Z']) == (player['X'], player['Y'], player['Z']):
            # play sound and update GUI to indicate fight has started
            pg_help.play_sound(con.start_fight_sound)
            pg_help.draw_one_line_text(screen, 'The creature emerges from the darkness...')
            pg_help.draw_image(screen, con.monster_img)
            fight.start_fight(screen, fight_inputs, player, monster)

    # if game loop was exited and player is still alive, then the player must have won
    if helpers.is_alive(player):
        # play monster death sound and update GUI to indicate player has won
        pg_help.play_sound(con.monster_death_sound)
        pg_help.draw_image(screen, con.win_img)
        pg_help.draw_one_line_text(screen, con.winning_end_msg_list)

    # if game loop is exited and monster is still alive, then the player must have lost
    elif helpers.is_alive(monster):
        # play player death sound and update GUI to indicate player has lost
        pg_help.play_sound(con.death_sound)
        pg_help.draw_image(screen, con.lose_img)
        pg_help.draw_one_line_text(screen, con.losing_end_msg_list)

    pg.quit()


def main():
    run_game()


if __name__ == '__main__':
    main()
