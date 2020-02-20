import sys

import pygame as pg

from ui.input import control


def check_keyboard_events(window, state):
    def close():
        pg.quit()
        sys.exit()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            close()

        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            close()

        elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
            control.central_button(window, state)
        elif event.type == pg.KEYDOWN and event.key == pg.K_UP:
            control.scroll_menu_up(window, state)
        elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
            control.scroll_menu_down(window, state)

        elif event.type == pg.KEYDOWN and event.key == pg.K_q:
            control.back(window, state)
        elif event.type == pg.KEYDOWN and event.key == pg.K_w:
            control.switch_led(window, state)
        elif event.type == pg.KEYDOWN and event.key == pg.K_e:
            control.switch_audio(window, state)
        elif event.type == pg.KEYDOWN and event.key == pg.K_r:
            control.open_setting(window, state)

        elif event.type == pg.KEYDOWN and event.key == pg.K_1:
            control.play_favourite(window, state, 1)
        elif event.type == pg.KEYDOWN and event.key == pg.K_2:
            control.play_favourite(window, state, 2)
        elif event.type == pg.KEYDOWN and event.key == pg.K_3:
            control.play_favourite(window, state, 3)
        elif event.type == pg.KEYDOWN and event.key == pg.K_4:
            control.play_favourite(window, state, 4)
        elif event.type == pg.KEYDOWN and event.key == pg.K_5:
            control.play_favourite(window, state, 5)
        elif event.type == pg.KEYDOWN and event.key == pg.K_6:
            control.play_favourite(window, state, 6)
        elif event.type == pg.KEYDOWN and event.key == pg.K_7:
            control.play_favourite(window, state, 7)
