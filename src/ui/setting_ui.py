from globals import *
from radio import player

import tkinter as tk


class SettingUI:

    def __init__(self, window, state):
        self.window = window
        self.setting_menu_entries(state)

    def setting_menu_entries(self, state):
        def selected_entry(station_):
            selected_entry_frame = tk.Frame(self.window, relief=tk.SOLID, bd=1, bg="#000000")
            if station_[0] is state.play_radio_station:
                playing_icon = tk.PhotoImage(file=RES_PATH + "icons/playing/playing_big.png")
                icon_label = tk.Label(selected_entry_frame, image=playing_icon, bg="#000000", font=(FONT_SEMIBOLD, 70), fg="#ffffff")
                icon_label.image = playing_icon
                icon_label.grid(row=0, column=0, sticky=tk.W, padx=10)
                tk.Label(selected_entry_frame, text=station_[1].upper(), bg="#000000", font=(FONT_SEMIBOLD, 70), fg="#ffffff").grid(row=0, column=1, sticky=tk.W)
            else:
                tk.Label(selected_entry_frame, text=station_[1].upper(), bg="#000000", font=(FONT_SEMIBOLD, 70), fg="#ffffff").grid(row=0, column=0, sticky=tk.W)
            selected_entry_frame.place(x=70, y=300)
            selected_entry_description_frame = tk.Frame(self.window, relief=tk.SOLID, bd=1, bg="#000000")
            # TODO set Label
            tk.Label(selected_entry_description_frame, text="test", bg="#000000", font=(FONT_REGULAR, 25), fg="#cccccc", padx=10).grid(row=0, column=0, sticky=tk.NW)
            selected_entry_description_frame.place(x=70, y=400)

        def unselected_entry(station_, count):
            if count < 0:
                y = 280 + (55 * count)
            else:
                y = 500 + (55 * count)

            if abs(count) is 1:
                color = "#cccccc"
            elif abs(count) is 2:
                color = "#999999"
            elif abs(count) is 3:
                color = "#676767"
            elif abs(count) is 4:
                color = "#454545"
            else:
                color = "#333333"
            selected_entry_frame = tk.Frame(self.window, relief=tk.SOLID, bd=1, bg="#000000")
            if station_[0] is state.play_radio_station:
                if count > 4 or count < -4:
                    count = 5
                playing_icon = tk.PhotoImage(file=RES_PATH + "icons/playing/playing" + str(abs(count)) + ".png")
                icon_label = tk.Label(selected_entry_frame, image=playing_icon, bg="#000000", font=(FONT_REGULAR, 40), fg=color)
                icon_label.image = playing_icon
                icon_label.grid(row=0, column=0, sticky=tk.W, padx=10)
                tk.Label(selected_entry_frame, text=station_[1].upper(), bg="#000000", font=(FONT_REGULAR, 40), fg=color).grid(row=0, column=1, sticky=tk.SW)
            else:
                tk.Label(selected_entry_frame, text=station_[1].upper(), bg="#000000", font=(FONT_REGULAR, 40), fg=color, padx=10).grid(row=0, column=0, sticky=tk.NW)
            selected_entry_frame.place(x=50, y=y)

        selected_entry(state.radio_stations[state.selected_radio_station_setting_ui])
        menu_down, menu_up = [], []

        for station in state.radio_stations[state.selected_radio_station_setting_ui + 1:]:
            menu_down.append(station)
        while len(menu_down) < 4:
            for station in state.radio_stations:
                menu_down.append(station)

        for station in reversed(state.radio_stations[:state.selected_radio_station_setting_ui]):
            menu_up.append(station)
        while len(menu_up) < 5:
            for station in reversed(state.radio_stations):
                menu_up.append(station)

        for num, station in enumerate(menu_down, start=1):
            unselected_entry(station, num)

        for num, station in enumerate(menu_up, start=1):
            unselected_entry(station, -num)





