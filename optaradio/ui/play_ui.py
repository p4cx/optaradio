import pygame as pg

from optaradio.globals import *
from optaradio.ui import bar


def run(window, state):
    window.fill(BLACK)
    station_cover(window, state)
    if state.setting_data['show_buttons']['status'] == "on":
        bar.add_bar(window, state)
    pg.display.flip()
    actual_station_song(window, state)


def actual_station_song(window, state):
    state.set_actual_playing_song(state)
    window.fill(BLACK)
    font = pg.font.Font(FONT_REGULAR_PATH, 45)
    playing_song = state.actual_playing_song[state.actual_playing_song_count]
    station_text = font.render(playing_song, True, WHITE)
    text_rect = station_text.get_rect(center=(WINDOW_WIDTH/2, 550))
    window.blit(station_text, text_rect)
    pg.display.update(pg.Rect((0, 500), (1000, 100)))


def station_cover(window, state):
    station_cover_path = RES_PATH + "radio_thumbs/" + state.radio_stations[state.play_radio_station][4]
    station_cover_image = pg.image.load(station_cover_path).convert()
    window.blit(station_cover_image, (0, 0))


def control_buttons(window, state):
    station_cover_path = RES_PATH + "radio_thumbs/" + state.radio_stations[state.play_radio_station][4]
    station_cover_image = pg.image.load(station_cover_path)
    window.blit(station_cover_image, (50, 10))
