import pygame as pg
import sys

def draw_windows(screen):
    pg.draw.rect(screen, (255, 255, 255), pg.Rect(20, 20, 1040, 480), 5)
    pg.draw.rect(screen, (169, 169, 169), pg.Rect(20, 515, 1040, 190), 5)
    pg.display.flip()


def draw_image(screen, image_path):
    img = pg.image.load(image_path).convert()
    transformed_img = pg.transform.scale(img, (1030, 470))
    screen.blit(transformed_img, (25, 25))
    pg.display.flip()


def draw_one_line_text(screen, msg_list, size=60, wait=False):
    # initialize font-style
    font = pg.font.Font('Fonts/Amatic-Bold.ttf', size)

    if type(msg_list) == str:
        # draw console background to replace previous text
        pg.draw.rect(screen, (0, 0, 0), pg.Rect(25, 520, 1030, 180))

        # render text
        text = font.render(msg_list, True, (255, 255, 255))
        text_rect = text.get_rect()

        # adjust text location and draw it
        text_rect.center = (520, 605)
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

        text_rect.center = (520, 605)
        screen.blit(text, text_rect)

        pg.display.flip()

        # make user press enter to continue
        wait_for_input([pg.K_RETURN])

    pg.draw.rect(screen, (0, 0, 0), pg.Rect(25, 520, 1030, 180))
    pg.display.flip()
    

def draw_multi_line_text(screen, msg_list, size=40):
    font = pg.font.Font('Fonts/Amatic-Bold.ttf', size)
    pg.draw.rect(screen, (0, 0, 0), pg.Rect(25, 520, 1030, 180))

    for index, msg in enumerate(msg_list):
        text = font.render(msg, True, (255, 255, 255))
        text_rect = text.get_rect()

        text_rect.center = (520, 605 + index * size)
        screen.blit(text, text_rect)

        pg.display.flip()


def play_sound(file_path):
    print(file_path)
    pg.mixer.music.load(file_path)
    pg.mixer.music.play()


def wait_for_input(valid_inputs):
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.KEYDOWN and event.key in valid_inputs:
                return event.key
