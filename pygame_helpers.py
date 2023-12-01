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


def draw_text(screen, msg_list, size):
    font = pg.font.Font('Fonts/Amatic-Bold.ttf', size)

    for msg in msg_list:
        pg.draw.rect(screen, (0, 0, 0), pg.Rect(25, 520, 1030, 180))
        text = font.render(msg, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (520, 605)
        press_enter_msg = font.render('Press Enter to Continue', True, (255, 255, 255))
        enter_msg_rect = press_enter_msg.get_rect()
        enter_msg_rect.center = (520, 610 + size)

        # make user press enter to continue
        while True:
            event = pg.event.wait()
            if event == pg.QUIT:
                pg.display.quit()
                pg.quit()
                sys.exit()

            if event == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    break
