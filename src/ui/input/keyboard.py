import pygame as pg

from radio import main

import sys


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
            central_button(window, state)
        elif event.type == pg.KEYDOWN and event.key == pg.K_UP:
            scroll_menu_up(window, state)
        elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
            scroll_menu_down(window, state)
        elif event.type == pg.KEYDOWN and event.key == pg.K_s:
            open_setting(window, state)
        elif event.type == pg.KEYDOWN and event.key == pg.K_c:
            clean_radio(window, state)
        elif event.type == pg.KEYDOWN and event.key == pg.K_1:
            play_favourite(window, state, 1)
        elif event.type == pg.KEYDOWN and event.key == pg.K_2:
            play_favourite(window, state, 2)
        elif event.type == pg.KEYDOWN and event.key == pg.K_3:
            play_favourite(window, state, 3)
        elif event.type == pg.KEYDOWN and event.key == pg.K_4:
            play_favourite(window, state, 4)
        elif event.type == pg.KEYDOWN and event.key == pg.K_5:
            play_favourite(window, state, 5)
        elif event.type == pg.KEYDOWN and event.key == pg.K_6:
            play_favourite(window, state, 6)


def central_button(window, state):
    if state.actual_ui is "start_ui":
        main.change_ui(window, state, "menu_ui")
    elif state.actual_ui is "menu_ui":
        if state.play_radio_station is not state.selected_radio_station_menu_ui:
            state.play_radio_station = state.selected_radio_station_menu_ui
            main.play(state)
        main.change_ui(window, state, "play_ui")
    elif state.actual_ui is "play_ui":
        main.stop(state)
        main.change_ui(window, state, "menu_ui")


def clean_radio(window, state):
    main.stop(state)
    if state.actual_ui is "menu_ui":
        main.change_ui(window, state, "start_ui")
    else:
        main.change_ui(window, state, "menu_ui")

def scroll_menu_up(window, state):
    if state.actual_ui is not "setting_ui":
        state.set_selected_radio_station(state, -1, "menu_ui")
        main.change_ui(window, state, "menu_ui")
    elif state.actual_ui is "setting_ui":
        state.set_selected_radio_station(state, -1, "setting_ui")
        main.change_ui(window, state, "setting_ui")


def scroll_menu_down(window, state):
    if state.actual_ui is not "setting_ui":
        state.set_selected_radio_station(state, 1, "menu_ui")
        main.change_ui(window, state, "menu_ui")
    elif state.actual_ui is "setting_ui":
        state.set_selected_radio_station(state, 1, "setting_ui")
        main.change_ui(window, state, "setting_ui")


def open_setting(window, state):
    if state.actual_ui is not "setting_ui":
        state.actual_ui = "setting_ui"
        main.change_ui(window, state, "setting_ui")
    else:
        state.actual_ui = "menu_ui"
        main.change_ui(window, state, "menu_ui")


def play_favourite(window, state, favourite_number):
    state.actual_ui = "play_ui"
    state.play_radio_station = favourite_number
    main.play(state)
    main.change_ui(window, state, "play_ui")
