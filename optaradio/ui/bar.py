import pygame as pg

from globals import *


def add_bar(window, state):
    color = "w"
    if state.actual_ui is "menu_ui":
        color = "g"
    elif state.actual_ui is "start_ui":
        color = "g"
    elif state.actual_ui is "play_ui":
        color = "w"
    elif state.actual_ui is "setting_ui":
        color = "g"

    setting_icon = pg.image.load(RES_PATH + "icons/bar/setting_" + color + ".png")
    window.blit(setting_icon, (955, 20))

    if state.setting_data['led']['status'] == "on":
        led_icon = pg.image.load(RES_PATH + "icons/bar/led_on_" + color + ".png")
    else:
        led_icon = pg.image.load(RES_PATH + "icons/bar/led_off_" + color + ".png")
    window.blit(led_icon, (900, 20))

    if state.setting_data['audio']['status'] == "on":
        audio_icon = pg.image.load(RES_PATH + "icons/bar/audio_on_" + color + ".png")
    else:
        audio_icon = pg.image.load(RES_PATH + "icons/bar/audio_off_" + color + ".png")
    window.blit(audio_icon, (845, 20))

    back_icon = pg.image.load(RES_PATH + "icons/bar/back_" + color + ".png")
    window.blit(back_icon, (790, 20))
