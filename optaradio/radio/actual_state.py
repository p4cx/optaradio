from radio import player
from ui.helper import cut_text
from globals_radio import *

import pygame as pg


class State:
    def __init__(
            self,
            actual_ui,
            radio_stations,
            selected_radio_station_menu_ui,
            selected_entry_setting_ui,
            play_radio_station,
            actual_playing_song,
            actual_playing_song_raw,
            actual_playing_song_count,
            setting_data):

        # main
        self.actual_ui = actual_ui

        # menu_ui
        self.radio_stations = radio_stations
        self.selected_radio_station_menu_ui = selected_radio_station_menu_ui
        self.selected_entry_setting_ui = selected_entry_setting_ui
        self.play_radio_station = play_radio_station
        self.actual_playing_song = actual_playing_song
        self.actual_playing_song_count = actual_playing_song_count
        self.actual_playing_song_raw = actual_playing_song_raw

        # settings
        self.setting_data = setting_data

    def set_selected_radio_station(self, value, ui):
        if ui is "menu_ui":
            if self.selected_radio_station_menu_ui is 0 and value is -1:
                self.selected_radio_station_menu_ui = len(self.radio_stations) - 1
            elif self.selected_radio_station_menu_ui is len(self.radio_stations) - 1 and value is 1:
                self.selected_radio_station_menu_ui = 0
            else:
                self.selected_radio_station_menu_ui += value
        elif ui is "setting_ui":
            if self.selected_entry_setting_ui is 0 and value is -1:
                self.selected_entry_setting_ui = len(list(self.setting_data.keys())) - 1
            elif self.selected_entry_setting_ui is len(list(self.setting_data.keys())) - 1 and value is 1:
                self.selected_entry_setting_ui = 0
            else:
                self.selected_entry_setting_ui += value

    def set_actual_playing_song(self):
        song = player.get_song(self.radio_stations[self.play_radio_station][2])

        if song != self.actual_playing_song_raw and song != '':
            self.actual_playing_song_raw = song
            self.actual_playing_song = cut_text.get_song_title(
                song, pg.font.Font(FONT_REGULAR_PATH, 45), WINDOW_WIDTH - 50)
            self.actual_playing_song_count = 0
        else:
            if len(self.actual_playing_song) is 0:
                self.actual_playing_song_raw = self.radio_stations[self.play_radio_station][1]
                self.actual_playing_song = [self.actual_playing_song_raw]
                self.actual_playing_song_count = 0
            elif len(self.actual_playing_song) > (self.actual_playing_song_count + 1):
                self.actual_playing_song_count += 1
            else:
                self.actual_playing_song_count = 0
