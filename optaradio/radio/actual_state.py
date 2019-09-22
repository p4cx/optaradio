from optaradio.radio import player
from optaradio.ui.helper import cut_text
from optaradio.globals import *
import pygame as pg

class State:

    def __init__(
            self,
            actual_ui,
            radio_stations,
            selected_radio_station_menu_ui,
            selected_radio_station_setting_ui,
            play_radio_station,
            actual_playing_song,
            actual_playing_song_raw,
            actual_playing_song_count):

        # main
        self.actual_ui = actual_ui

        # menu_ui
        self.radio_stations = radio_stations
        self.selected_radio_station_menu_ui = selected_radio_station_menu_ui
        self.selected_radio_station_setting_ui = selected_radio_station_setting_ui
        self.play_radio_station = play_radio_station
        self.actual_playing_song = actual_playing_song
        self.actual_playing_song_count = actual_playing_song_count
        self.actual_playing_song_raw = actual_playing_song_raw

    def set_selected_radio_station(self, value, ui):
        if ui is "menu_ui":
            if self.selected_radio_station_menu_ui is 0 and value is -1:
                self.selected_radio_station_menu_ui = len(self.radio_stations) - 1
            elif self.selected_radio_station_menu_ui is len(self.radio_stations) - 1 and value is 1:
                self.selected_radio_station_menu_ui = 0
            else:
                self.selected_radio_station_menu_ui += value
        elif ui is "setting_ui":
            if self.selected_radio_station_setting_ui is 0 and value is -1:
                self.selected_radio_station_setting_ui = len(self.radio_stations) - 1
            elif self.selected_radio_station_setting_ui is len(self.radio_stations) - 1 and value is 1:
                self.selected_radio_station_setting_ui = 0
            else:
                self.selected_radio_station_setting_ui += value

    def set_actual_playing_song(self):
        song = player.get_song(self.radio_stations[self.play_radio_station][2])
        if song != self.actual_playing_song_raw:
            self.actual_playing_song_raw = song
            self.actual_playing_song = cut_text.get_song_title(song, pg.font.Font(FONT_REGULAR_PATH, 45), WINDOW_WIDTH - 50)
            self.actual_playing_song_count = 0
            return True
        else:
            if len(self.actual_playing_song) > 1:
                return True
            else:
                return False
