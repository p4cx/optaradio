from src.globals import *

import tkinter as tk
import tkinter.font as tkfont

from src.ui.helper import cut_text


class MenuUI:

    def __init__(self, window, state):
        self.window = window
        self.menu_entries(state)

    def menu_entries(self, state):
        def selected_entry(station_):
            selected_entry_frame = tk.Frame(self.window, relief=tk.SOLID, bd=1, bg="#000")
            tk.Label(selected_entry_frame, text=station_[1].upper(), bg="#000", font=(FONT_SEMIBOLD, 70), fg="#fff").grid(row=0, column=0, sticky=tk.SW)
            text = cut_text.get_multi_line(station_[3], tkfont.Font(family=FONT_REGULAR, size=25), WINDOW_WIDTH-120)
            for num_, line in enumerate(text, start=1):
                tk.Label(selected_entry_frame, text=line, bg="#000", font=(FONT_REGULAR, 25), fg="#ccc", padx=10).grid(row=num_, column=0, sticky=tk.NW)
            selected_entry_frame.place(x=70, y=300)
            return len(text)

        def unselected_entry(station_, count, selected_description_length_):
            if count < 0:
                y = 280 + (55 * count)
            else:
                y = 420 + selected_description_length_ * 32 + (55 * count)

            if abs(count) is 1:
                color = "#ccc"
            elif abs(count) is 2:
                color = "#999"
            elif abs(count) is 3:
                color = "#676767"
            elif abs(count) is 4:
                color = "#454545"
            else:
                color = "#333"
            selected_entry_frame = tk.Frame(self.window, relief=tk.SOLID, bd=1, bg="#000")
            text = cut_text.get_first_line(station_[1].upper(), tkfont.Font(family=FONT_REGULAR, size=40), WINDOW_WIDTH-120)
            tk.Label(selected_entry_frame, text=text, bg="#000", font=(FONT_REGULAR, 40), fg=color, padx=10).grid(row=0, column=0, sticky=tk.NW)
            selected_entry_frame.place(x=50, y=y)

        selected_description_length = selected_entry(state.radio_stations[state.selected_radio_station])
        menu_down, menu_up = [], []

        for station in state.radio_stations[state.selected_radio_station + 1:]:
            menu_down.append(station)
        while len(menu_down) < 4:
            for station in state.radio_stations:
                menu_down.append(station)

        for station in reversed(state.radio_stations[:state.selected_radio_station]):
            menu_up.append(station)
        while len(menu_up) < 5:
            for station in reversed(state.radio_stations):
                menu_up.append(station)

        for num, station in enumerate(menu_down, start=1):
            unselected_entry(station, num, selected_description_length)

        for num, station in enumerate(menu_up, start=1):
            unselected_entry(station, -num, selected_description_length)



