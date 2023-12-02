import pygame as pg
import sys
import math

def draw_windows(screen):
    pg.draw.rect(screen, (255, 255, 255), pg.Rect(20, 20, 1040, 480), 5)
    pg.draw.rect(screen, (169, 169, 169), pg.Rect(20, 515, 1040, 190), 5)
    pg.display.flip()


def draw_image(screen, image_path):
    img = pg.image.load(image_path).convert()
    transformed_img = pg.transform.scale(img, (1030, 470))
    screen.blit(transformed_img, (25, 25))
    pg.display.flip()


def draw_one_line_text(screen, msg_list, size=40, wait=True):
    # initialize font-style
    font = pg.font.Font('Fonts/Amatic-Bold.ttf', size)

    if type(msg_list) == str:
        # draw console background to replace previous text
        pg.draw.rect(screen, (0, 0, 0), pg.Rect(25, 520, 1030, 180))

        # render text
        text = font.render(msg_list, True, (255, 255, 255))
        text_rect = text.get_rect()

        # adjust text location and draw it
        text_rect.center = (540, 605)
        screen.blit(text, text_rect)

        # update screen
        pg.display.flip()

        # wait for enter only if specified in call
        wait_for_input([pg.K_RETURN]) if wait == True else None
        return
    
    for msg in msg_list:
        pg.draw.rect(screen, (0, 0, 0), pg.Rect(25, 520, 1030, 180))

        text = font.render(msg, True, (255, 255, 255))
        text_rect = text.get_rect()

        text_rect.center = (540, 605)
        screen.blit(text, text_rect)

        pg.display.flip()

        # make user press enter to continue
        wait_for_input([pg.K_RETURN])

    pg.draw.rect(screen, (0, 0, 0), pg.Rect(25, 520, 1030, 180))
    pg.display.flip()
    

def draw_multi_line_text(screen, msg_list, size=40, wait=True):
    font = pg.font.Font('Fonts/Amatic-Bold.ttf', size)
    pg.draw.rect(screen, (0, 0, 0), pg.Rect(25, 520, 1030, 180))

    for index, msg in enumerate(msg_list):
        text = font.render(msg, True, (255, 255, 255))
        text_rect = text.get_rect()

        text_rect.center = (540, 520 + size / 2 + index * size)
        screen.blit(text, text_rect)

        pg.display.flip()
    wait_for_input([pg.K_RETURN]) if wait == True else None


def play_sound(file_path):
    print(file_path)
    pg.mixer.music.load(file_path)
    pg.mixer.music.play()


def wait_for_input(valid_inputs):
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key in valid_inputs:
                return event.key


def draw_map(screen, player, monster, board):
    board_row = list(board.keys())[-1][0] + 1
    board_col = list(board.keys())[-1][2] + 1
    board_height = player['Y']
    pg.draw.rect(screen, (0, 0, 0), pg.Rect(25, 25, 1030, 470))

    for z in range(board_col):
        for x in range(board_row):
            coord = (x, board_height, board_col - z - 1)
            if coord == (monster['X'], monster['Y'], monster['Z']):
                color = (255, 12, 69)
            elif coord  == (player['X'], player['Y'], player['Z']):
                color = (69, 230, 69)
            elif board[coord]['Event'] == 'None':
                if z % 2:
                    color = (69, 69, 69) if x % 2 else (88, 88, 88)
                else:
                    color = (88, 88, 88) if x % 2 else (69, 69, 69)
            elif board[coord]['Event'] == 'Salvage':
                color = (36, 132, 233)
            elif board[coord]['Event'] == 'Stairs':
                color = (255, 255, 84)
            elif board[coord]['Event'] == 'Holes':
                color = (255, 75, 255)

            rect_left = math.floor(25 + x * 1030 / board_row)
            rect_top = math.floor(25 + z * 470 / board_col)
            rect_width = math.floor(1030/ board_row)
            rect_height = math.floor(470 / board_col)
            pg.draw.rect(screen, color, pg.Rect(rect_left, rect_top, rect_width, rect_height))
            
    pg.display.flip()