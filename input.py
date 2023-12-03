import random
import helpers
import json
import os
import constants as con
import pygame as pg
import pygame_helpers as pg_help


def process_take(screen, player, board):
    """
    Process taking items from board

    :param screen: a pygame object that is the window of the game
    :param player: A dictionary that represents a player character
    :param board: A dictionary representing the playable area, populated with descriptions
    :precondition: player and board must be valid representations of their respective objects in the correct format
    :postcondition: After taking an item, the player's stats will increase based on what was taken
    :poscondition: The board at the coordinates will be changed to none-type event
    :return: A boolean value, returns True if an item was removed from the board, False otherwise
    """
    player_coords = (player['X'], player['Y'], player['Z'])
    board_event = board[player_coords]['Event']
    if board_event != 'Salvage':
        pg_help.draw_one_line_text(screen, 'There\'s nothing to take.', wait=False)
        return False

    random_number = random.randint(1, 20)
    if random_number == 4:
        fail_msg = 'You tried to grab the item, but fumbled in the darkness.'
        pg_help.draw_one_line_text(screen, fail_msg)
        new_description = 'There\'s nothing here but regret, since you fumbled grabbing the item'
        helpers.change_board_event(board, player_coords, 'None', new_description)
        return True

    # possible items: lid, bottle, knife, scissor, gun, armor
    atk_booster = ['bottle', 'knife', 'gun', 'scissor']
    def_booster = ['lid', 'armor']
    all_items = atk_booster + def_booster

    pg_help.play_sound(con.take_sound)
    for item in all_items:
        if item in board[player_coords]['Description']:
            pg_help.draw_image(screen, f'Images/{item}.jpg')
            pg_help.draw_one_line_text(screen, f'You managed to grab the {item} without issue.')
            player['ATK'] += 5 if item in atk_booster else 0
            player['DEF'] += 15 if item in def_booster else 0

            feedback_message = f'You now have increased offensive power with the {item}.' if item in atk_booster else\
                f'You now take less damage thanks to your {item}'
            pg_help.draw_one_line_text(screen, feedback_message)
            new_description = 'An empty void of darkness, it used to contain things, but you looted it.'
            helpers.change_board_event(board, player_coords, 'None', new_description)

    return True


def process_move(screen, player, monster, board, key_pressed):
    if key_pressed == pg.K_UP and board[(player['X'], player['Y'], player['Z'])]['Event'] != 'Stairs':
        pg_help.draw_one_line_text(screen, 'There\'s nothing to climb.', wait=False)
        return False

    elif key_pressed == pg.K_DOWN and board[(player['X'], player['Y'], player['Z'])]['Event'] != 'Hole':
        pg_help.draw_one_line_text(screen, 'There\'s no hole to jump into.', wait=False)
        return False

    elif helpers.out_of_bounds(player, board, key_pressed):
        pg_help.draw_one_line_text(screen, 'You bumped into a wall.', wait=False)
        return False

    if monster['Alerted']:
        trip_message = 'In your panic you tripped over some debris hidden in the darkness, you failed to move.'
        random_num = random.randint(1, 5)
        helpers.move(player, key_pressed) if random_num != 1 else pg_help.draw_one_line_text(screen, trip_message)
        pg_help.play_sound(con.chased_sound) if random_num != 1 else None

    else:
        if key_pressed == pg.K_UP:
            pg_help.play_sound(con.player_move_up_sound)
        elif key_pressed == pg.K_DOWN:
            pg_help.play_sound(con.player_move_down_sound)
        else:
            pg_help.play_sound(con.move_sound)
        helpers.move(player, key_pressed)

    return True


def process_flash(screen, player, monster, board):
    pg_help.draw_image(screen, con.flash_img)
    pg_help.play_sound(con.flash_sound)
    pg_help.draw_one_line_text(screen, 'You briefly shine your flashlight...')
    pg_help.draw_one_line_text(screen, 'You quickly take in what you see within the flash')
    pg_help.draw_map(screen, player, monster, board)
    pg_help.draw_multi_line_text(screen, con.flash_help_msg_list, size=25)
    if monster['Y'] != player['Y']:
        pg_help.draw_one_line_text(screen, 'You see no sign of the creature, it must be on a different floor.')
        return

    monster['Alerted'] = True
    monster['Alert Counter'] = 20
    
    pg_help.play_sound(con.alert_sound)
    alert_msg = 'You hear rabid snarling coming from the darkness, it seems you have alerted it to your presence.'
    pg_help.draw_one_line_text(screen, alert_msg)


def process_listen(screen, player, monster):
    pg_help.play_sound(con.player_listen_sound)
    pg_help.draw_one_line_text(screen, 'You stop everything and focus intensely on listening to your surroundings.')

    # process monster on different floor as player
    if player['Y'] > monster['Y']:
        pg_help.draw_one_line_text(
            screen, 'You pick up on some subtle shuffling on the floors below, the monster must be there...')
        return
    elif player['Y'] < monster['Y']:
        pg_help.draw_one_line_text(
            screen, 'You pick up some faint movement on the floors above, the monster must be there...')
        return

    direction = ''

    if player['Z'] < monster['Z']:
        direction += 'north'
    elif player['Z'] > monster['Z']:
        direction += 'south'
    if player['X'] < monster['X']:
        direction += 'west'
    elif player['X'] > monster['X']:
        direction += 'east'

    if direction:
        monster_location_description = f'You pick up faint sounds coming from {direction} of you.'
    else:
        monster_location_description = 'It\'s right behind you...'

    pg_help.draw_one_line_text(screen, monster_location_description)


def process_save(player, monster, board):
    file_num = 1
    file_path = os.path.join(os.path.dirname(__file__), 'saves')

    while os.path.exists(os.path.join(file_path, f'save-{file_num}.json')):
        file_num += 1

    if not os.path.exists(file_path):
        os.makedirs(file_path)
    
    with open(os.path.join(file_path, f'save-{file_num}.json'), 'w+') as save_file:
        stringed_board = helpers.convert_dictionary(board)
        json.dump([player, monster, stringed_board], save_file)


def process_load(screen):
    file_path = os.path.join(os.path.dirname(__file__), 'saves')

    save_numbers = helpers.get_saves_list()
    if not save_numbers:
        return None

    selected_save = pg_help.cycle_saves(screen, save_numbers)
    if not selected_save:
        return 'canceled'
    
    with open(os.path.join(file_path, f'save-{selected_save}.json')) as save_file:
        save_data = json.load(save_file)

    return save_data


def process_delete(screen):
    file_path = os.path.join(os.path.dirname(__file__), 'saves')

    save_numbers = helpers.get_saves_list()
    if not save_numbers:
        return False

    selected_save = pg_help.cycle_saves(screen, save_numbers)
    if not selected_save:
        return 'canceled'

    os.remove(os.path.join(file_path, f'save-{selected_save}.json'))

    return True
