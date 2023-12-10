"""
Jonathan Liu
A01375621
"""
import pygame as pg
import constants as con
import sys
import math
import random
import itertools


def draw_windows(screen: pg.SurfaceType) -> None:
    """
    Draw the window frames on the pygame window

    This function will draw the text and image frames on the passed in pygame window

    :param screen: A pygame surface object which represents the game window
    :precondition: screen must be a pygame surface object that represents the game window
    :postcondition: A white and grey border is drawn onto the game window
    """
    pg.draw.rect(screen, (255, 255, 255), pg.Rect(20, 20, 1040, 480), 5)
    pg.draw.rect(screen, (169, 169, 169), pg.Rect(20, 515, 1040, 190), 5)
    pg.display.flip()


def draw_image(screen: pg.SurfaceType, image_path: str) -> None:
    """
    Draw an image onto window

    This function draws the image located at the image file path onto the game window

    :param screen: A pygame surface object that represents the game window
    :param image_path: A string that represents the file path towards an image
    :precondition: screen must a pygame surface object that represents the game window
    :precondition: image_path must be a valid file path that leads to an existing image file
    :postcondition: An image is drawn onto the game window that is loaded from the file path
    """
    img = pg.image.load(image_path).convert()
    transformed_img = pg.transform.scale(img, (1030, 470))
    screen.blit(transformed_img, (25, 25))
    pg.display.flip()


def draw_one_line_text(screen: pg.SurfaceType, msg_list: str or list[str] or tuple[str], size=40, wait=True) -> None:
    """
    Draw text onto game window one line at a time

    This function draws a passed in str or list of strings, and draws them onto the game window one line at a time.

    :param screen: A pygame surface object that represents the game window
    :param msg_list: A string or a list of strings that is drawn onto the game window
    :param size: An integer that represents the font size to draw the text at, defaults to size 40
    :param wait: A boolean to determine if the player needs to press enter to continue, defaults to True
    :precondition: screen must be a pygame surface object that represents the game window
    :precondition: msg_list must either be a list/tuple of only strings or it can be a string
    :postcondition: The inputted messages are drawn onto the game window one line at a time
    :postcondition: The function will wait for the player to press enter to continue, if wait set to True
    """
    # initialize font-style
    font = pg.font.Font('Fonts/Amatic-Bold.ttf', size)

    # draw console background to replace previous text
    pg.draw.rect(screen, (0, 0, 0), pg.Rect(25, 520, 1030, 180))

    # set up different color prompts in which players need to press enter
    color = (255, 255, 255) if not wait else (255, 255, 145)

    if type(msg_list) == str:

        # render text
        text = font.render(msg_list, True, color)
        text_rect = text.get_rect()

        # adjust text location and draw it
        text_rect.center = (540, 605)
        screen.blit(text, text_rect)

        # update screen
        pg.display.flip()

        # wait for enter only if specified in call
        wait_for_input([pg.K_RETURN]) if wait is True else None
        return
    
    for msg in msg_list:
        pg.draw.rect(screen, (0, 0, 0), pg.Rect(25, 520, 1030, 180))

        text = font.render(msg, True, color)
        text_rect = text.get_rect()

        text_rect.center = (540, 605)
        screen.blit(text, text_rect)

        pg.display.flip()

        # make user press enter to continue
        wait_for_input([pg.K_RETURN])

    pg.draw.rect(screen, (0, 0, 0), pg.Rect(25, 520, 1030, 180))
    pg.display.flip()
    

def draw_multi_line_text(screen: pg.SurfaceType, msg_list: tuple[str] or list[str], size=40, wait=True) -> None:
    """
    Draw a lines of text onto the window

    This function draws all text within a list onto the game window all at once

    :param screen: A pygame surface object that represents the game window
    :param msg_list: A list of strings that represents the messages that need to be drawn
    :param size: An integer that determines the font size to draw the text at, defaults to 40
    :param wait: A boolean that determines if the player needs to press enter to continue, defaults to True
    :precondition: screen must be a pygame surface object that represents the game window
    :precondition: msg_list must be a list or tuple of only strings
    :postcondition: The inputted list of strings will be drawn onto the window, stacked on top of each other
    :postcondition: The function will wait for the player to press enter to continue, if wait set to True
    """
    font = pg.font.Font('Fonts/Amatic-Bold.ttf', size)
    pg.draw.rect(screen, (0, 0, 0), pg.Rect(25, 520, 1030, 180))

    for index, msg in enumerate(msg_list):
        text = font.render(msg, True, (255, 255, 255))
        text_rect = text.get_rect()

        text_rect.center = (540, 520 + size / 2 + index * size)
        screen.blit(text, text_rect)

        pg.display.flip()
    wait_for_input([pg.K_RETURN]) if wait is True else None


def play_sound(file_path: str) -> None:
    """
    Play a sound

    This function plays the sound located at the given file path

    :param file_path: A string that represents the file path towards a sound file
    :precondition: file_path must be a valid file path towards an existing sound file
    :postcondition: The sound file will be played within the game
    """
    pg.mixer.music.load(file_path)
    pg.mixer.music.play()


def wait_for_input(valid_inputs: list[int] or tuple[int]) -> int:
    """
    Wait for player input

    This function will enter a cycle and wait for the player to press one of the valid key numbers that was passed
    into the function.

    :param valid_inputs: A list of pygame key constants that represents the allowed keys the player can press
    :precondition: valid_inputs must be a list or tuple of only pygame key constants
    :postcondition: The game will stall until the player hits an allowed key press
    :return: The pygame constant that represents the key the player has pressed
    """
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key in valid_inputs:
                return event.key


def draw_map(screen: pg.SurfaceType, player: dict, monster: dict, board: dict) -> None:
    """
    Draw map on pygame

    This function will draw a grid map of the floor that the player is currently at

    :param screen: A pygame surface object that must represent the game window
    :param player: A dictionary that represents the player
    :param monster: A dictionary that represents the monster
    :param board: A dictionary that represents the playable area
    :precondition: All parameters must be accurate reflections of what they represent, and must be correctly formatted
    :postcondition: A grid map of the floor the player is on is drawn onto the game window
    """
    board_row = list(board.keys())[-1][0] + 1
    board_col = list(board.keys())[-1][2] + 1
    board_height = player['Y']
    pg.draw.rect(screen, (0, 0, 0), pg.Rect(25, 25, 1030, 470))

    # set up cycle of different color to print different colors
    default_colors = itertools.cycle(((69, 69, 69), (88, 88, 88)))

    for z in range(board_col):
        for x in range(board_row):
            coord = (x, board_height, board_col - z - 1)
            color = default_colors.__next__()
            if coord == (monster['X'], monster['Y'], monster['Z']):
                color = (255, 12, 69)
            elif coord == (player['X'], player['Y'], player['Z']):
                color = (69, 230, 69)
            elif board[coord]['Event'] == 'Salvage':
                color = (36, 132, 233)
            elif board[coord]['Event'] == 'Stairs':
                color = (255, 255, 84)
            elif board[coord]['Event'] == 'Hole':
                color = (255, 75, 255)

            rect_left = math.floor(25 + x * 1030 / board_row)
            rect_top = math.floor(25 + z * 470 / board_col)
            rect_width = math.floor(1030 / board_row)
            rect_height = math.floor(470 / board_col)
            pg.draw.rect(screen, color, pg.Rect(rect_left, rect_top, rect_width, rect_height))

        default_colors.__next__()

    pg.display.flip()


def cycle_saves(screen: pg.SurfaceType, save_list: list[int]) -> int or None:
    """
    Cycle through save files

    This function will allow the user to cycle through the list of save files found in the saves directory,
    and allow them to select a save that they wish to select.

    :param screen: A pygame surface object that represents the game window
    :param save_list: A list of integers that represents the existing save labels found in the saves directory
    :precondition: screen must be a pygame surface object that represents the game window
    :precondition: save_list must be a list of integers that correspond to existing save labels in the saves directory
    :postcondition: Correctly formatted file names is drawn onto the game window
    :postcondition: The function will stall and wait for the player to input something to navigate the menu
    :return: An integer representing the player's choice is returned if selected, otherwise return None
    """
    valid_inputs, index = (pg.K_UP, pg.K_DOWN, pg.K_RETURN, pg.K_ESCAPE), 0
    selected_save = save_list[index]
    while True:
        draw_one_line_text(screen, f'Selected Save: Save-{selected_save}', wait=False)
        key_pressed = wait_for_input(valid_inputs)
        if key_pressed == pg.K_RETURN:
            return selected_save
        elif key_pressed == pg.K_DOWN:
            index += 1
            try:
                selected_save = save_list[index]
            except IndexError:
                index = 0
                selected_save = save_list[index]

        elif key_pressed == pg.K_UP:
            index -= 1
            index = len(save_list) - 1 if index < 0 else index
            selected_save = save_list[index]

        elif key_pressed == pg.K_ESCAPE:
            return


def play_random_ambience() -> None:
    """
    Play a random sound file

    This function will have a 1 in 7 chance of playing a random sound from a list of sound file paths

    :precondition: The sound file paths in the list must lead to an existing sound file
    :postcondition: A sound will have a 1 in 7 chance of playing a sound from a list of 3 different sound files
    """
    random_number = random.randint(1, 7)
    if random_number == 4:
        random_ambience_choice = random.randint(0, 2)
        play_sound(con.ambience_list[random_ambience_choice])
