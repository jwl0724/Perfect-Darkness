"""
Jonathan Liu
A01375621
"""
import random
import helpers
import json
import os
import constants as con
import pygame as pg
import pygame_helpers as pg_help


def process_take(screen: pg.SurfaceType, player: dict, board: dict) -> bool:
    """
    Process taking items from board

    This function will attempt to remove 'Salvage' type events from the board and replace them with 'None' type
    events, after which the player stats will increase depending on what item was at the spot and messages will be
    drawn on the pygame screen to indicate an item is removed from the board. If the location is not a 'Salvage' type
    event, then a message is drawn on the pygame screen and nothing occurs.

    :param screen: a pygame object that is the window of the game
    :param player: A dictionary that represents a player character
    :param board: A dictionary representing the playable area, populated with an event type identifier and a description
    :precondition: player and board must be valid representations of their respective objects in the correct format
    :precondition: board must contain event types that are valid within the game itself
    :precondition: board description must be a string that contains one of the possible items within the game
    :postcondition: After taking an item, the player's stats will increase based on what was taken
    :postcondition: The board at the coordinates will be changed to none-type event
    :return: A boolean value, returns True if an item was removed from the board, False otherwise
    """
    player_coords = (player['X'], player['Y'], player['Z'])
    board_event = board[player_coords]['Event']

    # return False if the board event is not salvage type
    if board_event != 'Salvage':
        pg_help.draw_one_line_text(screen, 'There\'s nothing to take.', wait=False)
        return False

    # 1 in 20 chance that picking up an item fails
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

    # play take sfx
    pg_help.play_sound(con.take_sound)

    for item in all_items:
        # increase player stat and draw message on pygame window depending on the item at the location is
        if item in board[player_coords]['Description']:
            pg_help.draw_image(screen, f'Images/{item}.jpg')
            pg_help.draw_one_line_text(screen, f'You managed to grab the {item} without issue.')
            player['ATK'] += 5 if item in atk_booster else 0
            player['DEF'] += 15 if item in def_booster else 0

            feedback_message = f'You now have increased offensive power with the {item}.' if item in atk_booster else\
                f'You now take less damage thanks to your {item}'
            pg_help.draw_one_line_text(screen, feedback_message)

            # update board to remove item from the board
            new_description = 'An empty void of darkness, it used to contain things, but you looted it.'
            helpers.change_board_event(board, player_coords, 'None', new_description)

            return True


def process_move(screen: pg.SurfaceType, player: dict, monster: dict, board: dict, key_pressed: int) -> bool:
    """
    Process player movement

    This function takes the key that was pressed in the game and translates it to a direction, then it  will evaluate if
    the direction will cause the player to go out of bounds, if yes then the function stops there, if no then the
    function will proceed to move the player in inputted direction depending, with a chance to fail if the monster is
    chasing the player. The pygame window will also draw text to reflect any failures in movement, and successful
    movements will play a sound.

    :param screen: A pygame surface object which represents the game window
    :param player: A dictionary representing the player
    :param monster: A dictionary representing the monster
    :param board: A dictionary representing the playable area
    :param key_pressed: A pygame constant that represents a key that was pressed
    :precondition: All parameters must correctly reflect what they are supposed to represent in the correct formatting
    :postcondition: The pygame window will have text drawn onto it
    :postcondition: A sound file will be played when movement is successful
    :postcondition: The player's coordinates will change if movement was successful
    :return: A boolean False if the inputted direction is invalid, True otherwise
    """
    # when up is pressed when not at stairs
    if key_pressed == pg.K_UP and board[(player['X'], player['Y'], player['Z'])]['Event'] != 'Stairs':
        pg_help.draw_one_line_text(screen, 'There\'s nothing to climb.', wait=False)
        return False

    # when down is pressed when not at holes
    elif key_pressed == pg.K_DOWN and board[(player['X'], player['Y'], player['Z'])]['Event'] != 'Hole':
        pg_help.draw_one_line_text(screen, 'There\'s no hole to jump into.', wait=False)
        return False

    # when movement results in going out of bounds
    elif helpers.out_of_bounds(player, board, key_pressed):
        pg_help.draw_one_line_text(screen, 'You bumped into a wall.', wait=False)
        return False

    # play different sfx and have a 20% chance to fail in movement when being chased
    if monster['Alerted']:
        trip_message = 'In your panic you tripped over some debris hidden in the darkness, you failed to move.'
        random_num = random.randint(1, 5)
        helpers.move(player, key_pressed) if random_num != 1 else pg_help.draw_one_line_text(screen, trip_message)
        pg_help.play_sound(con.chased_sound) if random_num != 1 else None

    # player normal sfx and move the player in the inputted direction
    else:
        if key_pressed == pg.K_UP:
            pg_help.play_sound(con.player_move_up_sound)
        elif key_pressed == pg.K_DOWN:
            pg_help.play_sound(con.player_move_down_sound)
        else:
            pg_help.play_sound(con.move_sound)
        helpers.move(player, key_pressed)

    return True


def process_flash(screen: pg.SurfaceType, player: dict, monster: dict, board: dict) -> None:
    """
    Process flashlight mechanic

    This function will draw a flashlight image, followed by a grid map of the player's current floor, and if the
    monster is on the same floor as the player, set the monster's "Alerted" property to True and set the chase
    counter to be 20 turns.

    :param screen: A pygame surface object that represents the game window
    :param player: A dictionary that represents the player
    :param monster: A dictionary the represents the monster
    :param board: A dictionary that represents the playable area
    :precondition: All parameters must accurately reflect their representations with correct formatting
    :postcondition: An image file will be drawn onto the pygame window, followed by a grid representing the map
    :postcondition: A sound file will be played during the functions process
    :postcondition: Text will be drawn onto the pygame window
    :postcondition: Monster "Alerted" property will be set to True and "Alert_Counter" set to 20 if monster is present
    """
    # draw flash, play sfx, and draw message for it
    pg_help.draw_image(screen, con.flash_img)
    pg_help.play_sound(con.flash_sound)
    pg_help.draw_one_line_text(screen, 'You briefly shine your flashlight...')
    pg_help.draw_one_line_text(screen, 'You quickly take in what you see within the flash')

    # draw the map and a legend
    pg_help.draw_map(screen, player, monster, board)
    pg_help.draw_multi_line_text(screen, con.flash_help_msg_list, size=25)

    # draw the creature is missing message
    if monster['Y'] != player['Y']:
        pg_help.draw_one_line_text(screen, 'You see no sign of the creature, it must be on a different floor.')
        return

    # alert the monster
    monster['Alerted'] = True
    monster['Alert_Counter'] = 20
    pg_help.play_sound(con.alert_sound)
    alert_msg = 'You hear rabid snarling coming from the darkness, it seems you have alerted it to your presence.'
    pg_help.draw_one_line_text(screen, alert_msg)


def process_listen(screen: pg.SurfaceType, player: dict, monster: dict) -> None:
    """
    Process listening mechanic

    This function will draw a text of where the monster is relative to the player's location onto the pygame window.

    :param screen: A pygame surface object that represents the game window
    :param player: A dictionary that represents a player
    :param monster: A dictionary that represents the monster
    :precondition: All parameters must accurately reflect what they represent with correct formatting
    :postcondition: A sound file will be played and text will be drawn onto the pygame window
    :return:
    """
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

    # concatenate the direction of where the monster is
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


def process_save(player: dict, monster: dict, board: dict) -> None:
    """
    Saves player's current session

    This function takes the player, monster, and board parameters and saves them into a json file that is placed
    within the saves directory, and if the directory does not exist then it will create the saves directory and
    place the new file into it.

    :param player: A dictionary representing the player
    :param monster: A dictionary representing the monster
    :param board: A dictionary representing the playable area
    :precondition: All parameters must accurately reflect what they represent and in the correct formatting
    :postcondition: A directory called saves is created if said directory does not exist
    :postcondition: A new json file containing the parameters properties is created
    :postcondition: A new dictionary is temporarily created with the tuple key converted into a string
    """
    file_num = 1
    file_path = os.path.join(os.path.dirname(__file__), 'saves')

    while os.path.exists(os.path.join(file_path, f'save-{file_num}.json')):
        file_num += 1

    if not os.path.exists(file_path):
        os.makedirs(file_path)
    
    with open(os.path.join(file_path, f'save-{file_num}.json'), 'w+') as save_file:
        stringed_board = helpers.convert_dictionary(board)
        json.dump([player, monster, stringed_board], save_file)


def process_load(screen: pg.SurfaceType) -> None | str | dict:
    """
    Load a player's previous save

    This function looks into the directory called saves and allows the player to cycle through all the saves within
    the directory, and choose which file to load.

    :param screen: A pygame surface object that represents the game window
    :precondition: screen must be a valid pygame surface object that represents the game window
    :postcondition: The selected save data will be read and retrieved
    :return: None is returned if no saves were found or if the saves directory does not exist
    :return: The string 'canceled' is returned if the user presses the escape key while cycling through saves
    :return: A list containing dictionaries representing the player, monster, and board with stringed keys is
    returned if save files were found and selected
    """
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


def process_delete(screen: pg.SurfaceType) -> False or str or True:
    """
    Delete a save file

    This function looks into the saves directory and allows the player to cycle through all the saves within the
    directory and choose which file to be deleted

    :param screen: A pygame surface object that represents the game window
    :precondition: screen must be a valid pygame surface object that represents the game window
    :postcondition: The selected save file will be deleted from the saves directory
    :return: boolean False is returned if no save files were found, or if the saves directory does not exist
    :return: boolean True is returned if a save file was found and was deleted from the directory.
    :return: The string 'canceled' is returned if the player presses escape while cycling through save files
    """
    file_path = os.path.join(os.path.dirname(__file__), 'saves')

    save_numbers = helpers.get_saves_list()
    if not save_numbers:
        return False

    selected_save = pg_help.cycle_saves(screen, save_numbers)
    if not selected_save:
        return 'canceled'

    os.remove(os.path.join(file_path, f'save-{selected_save}.json'))

    return True
