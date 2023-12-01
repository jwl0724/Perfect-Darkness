import pygame
from PIL import ImageTk, Image
import initialization as init
import mechanics as mech
import monster as mon
import helpers
import input as ipt
import pygame as pg


def run_game():
    # set initial variables
    player_stats, monster_stats = (10, 1, 0), (40, 5, 10)
    player_coords, monster_coords = (2, 0, 0), (2, 2, 4)
    rows, height, column = 5, 3, 5
    game_running = True

    # set constants
    VALID_ACTIONS = ('help', 'take', 'move', 'listen', 'flash', 'save', 'load', 'delete')

    # initialize the game
    player = init.create_entity(player_stats, player_coords, 1, True)
    monster = init.create_entity(monster_stats, monster_coords, 2, False)
    building = init.make_board(rows, height, column)

    # initialize pygame screen
    screen = pg.display.set_mode((1080, 720))
    pg.display.set_caption('Perfect Darkness')
    screen.fill((255, 255, 255))

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