import pygame
from PIL import ImageTk, Image
import initialization as init
import mechanics as mech
import monster as mon
import helpers
import input as ipt
import pygame as pg
import pygame_helpers as pg_help
import descriptions as desc

def run_game():
    # set initial variables
    player_stats, monster_stats = (10, 1, 0), (40, 5, 10)
    player_coords, monster_coords = (2, 0, 0), (2, 2, 4)
    rows, height, column = 5, 3, 5
    game_running = True

    # set file image and audio file paths
    knife_img, armor_img, bottle_img = 'Images/knife.jpg', 'Images/armor.jpg', 'Images/bottle.jpg'
    gun_img, lid_img, scissor_img = 'Images/gun.jpg', 'Images/lid.jpg', 'Images/scissor.jpg'
    monster_img, default_img, flash_img = 'Images/monster.jpg', 'Images/default.jpg', 'Images/flash.jpg'

    intro_msg = """
    Welcome to Perfect Darkness, you are a captured convict sent into a building under sanction. You are tasked 
    with eliminating the creature confined within the building. The foundation has not provided any tools or weapons 
    to help in your task, armed with nothing but your wits and flashlight, you must scour through the building to find 
    any semblance of equipment to help you in your task. But be careful, the building is in complete darkness with no 
    hopes of seeing the creature. You must rely on the subtle sounds the creature makes as it roams around, 
    looking for prey within it's domain. If at any point you wish to bring up a list of commands, type help.
    """

    # set constants
    VALID_ACTIONS = ('help', 'take', 'move', 'listen', 'flash', 'save', 'load', 'delete')

    # initialize the game
    player = init.create_entity(player_stats, player_coords, 1, True)
    monster = init.create_entity(monster_stats, monster_coords, 2, False)
    building = init.make_board(rows, height, column)

    # initialize pygame resources
    pg.init()
    screen = pg.display.set_mode((1080, 720))
    pg.display.set_caption('Perfect Darkness')
    screen.fill((0, 0, 0))
    pg_help.draw_windows(screen)
    pg_help.draw_image(screen, monster_img)
    pg_help.draw_text(screen, desc.intro, 60)
    pg.display.flip()

    while game_running:
        event = pg.event.wait()
        if event.type == pg.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            pass

    pg.quit()


def main():
    run_game()


if __name__ == '__main__':
    main()