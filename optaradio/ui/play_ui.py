import pygame as pg

from globals import *
from ui.helper import cut_text


def run(window, state):
    window.fill(BLACK)
    station_cover(window, state)
    #control_buttons(window, state)
    pg.display.flip()
    actual_station(window, state)
    actual_station_song(window, state)


def actual_station(window, state):
    font = pg.font.Font(FONT_SEMIBOLD_PATH, 75)
    station_text = font.render(state.radio_stations[state.play_radio_station][1].upper(), True, WHITE)
    window.blit(station_text, (50, 420))
    pg.display.update(pg.Rect((0, 430), (1000, 75)))


def actual_station_song(window, state):
    update = state.set_actual_playing_song(state)
    if update:
        #window.fill(BLACK)
        font = pg.font.Font(FONT_REGULAR_PATH, 35)
        playing_song = cut_text.get_first_line(state.actual_playing_song, pg.font.Font(FONT_REGULAR_PATH, 30),
                                               WINDOW_WIDTH - 60)
        station_text = font.render(playing_song, True, WHITE)
        window.blit(station_text, (50, 520))
        pg.display.update(pg.Rect((0, 530), (1000, 35)))


def station_cover(window, state):
    station_cover_path = RES_PATH + "radio_thumbs/" + state.radio_stations[state.play_radio_station][4]
    station_cover_image = pg.image.load(station_cover_path).convert()
    window.blit(station_cover_image, (50, 10))


def control_buttons(window, state):
    station_cover_path = RES_PATH + "radio_thumbs/" + state.radio_stations[state.play_radio_station][4]
    station_cover_image = pg.image.load(station_cover_path)
    window.blit(station_cover_image, (50, 10))