import time as t

import pygame as pg

from globals import *
from radio import weather


def run(window):
    window.fill(BLACK)
    pg.display.flip()
    add_time(window)
    add_weather(window)


def add_time(window):
    font = pg.font.Font(FONT_REGULAR_PATH, 250)
    text = font.render(str((t.strftime("%H:%M"))), True, WHITE)
    window.fill(BLACK)
    window.blit(text, (50, 50))
    pg.display.update(pg.Rect((0, 130), (1000, 180)))


def add_weather(window):
    weather_text_temp, weather_text_desc, icon_code = weather.get_weather()
    window.fill(BLACK)

    if icon_code is not "error":
        weather_icon_path = RES_PATH + 'icons/weather/' + icon_code + '.png'
        weather_icon = pg.image.load(weather_icon_path)
        window.blit(weather_icon, (70, 370))

    font = pg.font.Font(FONT_SEMIBOLD_PATH, 95)
    text = font.render(weather_text_temp, True, WHITE)
    window.blit(text, (230, 350))

    font = pg.font.Font(FONT_REGULAR_PATH, 60)
    text = font.render(weather_text_desc, True, WHITE)
    window.blit(text, (230, 450))

    pg.display.update(pg.Rect((0, 370), (1000, 180)))
