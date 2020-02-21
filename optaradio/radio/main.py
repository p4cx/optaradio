import pygame as pg

from optaradio.globals import *
from optaradio.radio import actual_state, station_list, player, loop
from optaradio.ui import start_ui, menu_ui, play_ui, setting_ui
from optaradio.ui.helper import cut_text, setting_handler


def run():
    pg.init()
    pg.display.set_caption('optaradio')
    pg.display.set_icon(pg.image.load(APP_ICON))
    window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    window.fill([30, 30, 230])

    pg.font.init()

    clock = pg.time.Clock()
    clock.tick(60)

    state = actual_state.State
    state.actual_ui = "start_ui"

    state.radio_stations = get_prepare_radio_stations()
    state.setting_data = setting_handler.load_settings_data()
    state.selected_radio_station_menu_ui = 0
    state.selected_entry_setting_ui = 0

    state.play_radio_station = -1
    state.actual_playing_song = []
    state.actual_playing_song_raw = ""
    state.actual_playing_song_count = 0

    change_ui(window, state, state.actual_ui)

    loop.run_loop(window, state)


def change_ui(window, state, ui_type):
    if ui_type is "menu_ui":
        state.actual_ui = "menu_ui"
        menu_ui.run(window, state)
    elif ui_type is "start_ui":
        state.actual_ui = "start_ui"
        start_ui.run(window, state)
    elif ui_type is "play_ui":
        state.actual_ui = "play_ui"
        play_ui.run(window, state)
    elif ui_type is "setting_ui":
        state.actual_ui = "setting_ui"
        setting_ui.run(window, state)
    if ui_type is not "play_ui":
        state.actual_playing_song = ""


def update_ui(window, state, element):
    if state.actual_ui == "start_ui":
        if element is "clock":
            start_ui.add_time(window)
        elif element is "weather":
            start_ui.add_weather(window)
    elif state.actual_ui == "play_ui":
        play_ui.actual_station_song(window, state)


def play(state):
    if not player.change_station(state.radio_stations[state.play_radio_station][2]):
        stop(state)
        return False
    else:
        return True


def stop(state):
    player.stop()
    state.actual_playing_song = []
    state.play_radio_station = -1


def get_prepare_radio_stations():
    radio_stations = station_list.get_station_list()
    for station in radio_stations:
        station[3] = cut_text.get_multi_line(station[3], pg.font.Font(FONT_REGULAR_PATH, 25), WINDOW_WIDTH - 120)

    return radio_stations


def set_led(window, state):
    setting_handler.set_setting(state, 'led')
    change_ui(window, state, state.actual_ui)


def set_audio(window, state):
    setting_handler.set_setting(state, 'audio')
    change_ui(window, state, state.actual_ui)


def switch_setting(state):
    setting_handler.set_setting(state, state.selected_entry_setting_ui)
