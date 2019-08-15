import tkinter as tk
from src.ui import start_ui, menu_ui, play_ui, setting_ui
from src.ui.input import keyboard, pi_pins
from src.globals import *
from src.radio import actual_state, station_list, player


def run():
    window = tk.Tk()
    window.geometry('{}x{}+{}+{}'.format(
        WINDOW_WIDTH,
        WINDOW_HEIGHT,
        int((window.winfo_screenwidth() / 2) - (WINDOW_WIDTH / 2)),
        int((window.winfo_screenheight() / 2) - (WINDOW_HEIGHT / 2))
    ))
    window.configure(background="#000")
    if WINDOW_FULL_SCREEN:
        window.attributes('-fullscreen', True)

    state = actual_state.State

    keyboard.bind_keys(window, state)

    state.radio_stations = station_list.get_station_list()
    state.selected_radio_station = 0


    # pi_pins.bind_pins()

    change_ui(window, state, "start_ui")

    window.mainloop()


def change_ui(window, state, ui_type):

    def set_ui__destroy_window(window_):
        state.actual_ui = ui_type
        for widget in window_.winfo_children():
            widget.destroy()

    if ui_type is "menu_ui":
        set_ui__destroy_window(window)
        menu_ui.MenuUI(window, state)
    elif ui_type is "start_ui":
        set_ui__destroy_window(window)
        start_ui.StartUI(window)
    elif ui_type is "play_ui":
        set_ui__destroy_window(window)
        play_ui.PlayUI(window, state)


def play(state):
    player.change_station(state.radio_stations[state.play_radio_station][2])


def stop():
    player.stop()
