from src.radio import weather
from src.globals import *

import tkinter as tk
import time as t


class StartUI:

    def __init__(self, window):
        self.window = window

        self.refresh_time()
        self.refresh_weather()

    def add_time(self, old_time_frame=None):
        time_frame = tk.Frame(self.window, relief=tk.SOLID, bd=1, bg="#000")
        time_data = t.strftime("%H:%M")

        tk.Label(time_frame, text=time_data, bg="#000", font=(FONT_SEMIBOLD, 260), fg="#fff").pack()

        time_frame.place(x=50, y=30)
        if old_time_frame is not None:
            old_time_frame.destroy()
        return time_frame

    def refresh_time(self, time_frame=None):
        time_frame = self.add_time(time_frame)
        time_frame.after(TIME_UPDATE_INTERVAL, self.refresh_time, time_frame)

    def add_weather(self, old_weather_frame=None):
        weather_frame = tk.Frame(self.window, relief=tk.SOLID, bd=1, bg="#000")
        weather_data = weather.get_weather()

        weather_icon = tk.PhotoImage(file=RES_PATH + "icons/weather/" + weather_data[2] + ".png")
        icon_label = tk.Label(weather_frame, image=weather_icon, bg="#000")
        icon_label.image = weather_icon
        icon_label.grid(row=0, column=0, rowspan=2, sticky=tk.W, padx=30)
        tk.Label(weather_frame, text=weather_data[0], bg="#000", font=(FONT_SEMIBOLD, 55), fg="#fff").grid(row=0, column=1, sticky=tk.SW)
        tk.Label(weather_frame, text=weather_data[1].upper(), bg="#000", font=(FONT_REGULAR, 32), fg="#fff").grid(row=1, column=1, sticky=tk.NW)

        weather_frame.place(x=50, y=380)
        if old_weather_frame is not None:
            old_weather_frame.destroy()
        return weather_frame

    def refresh_weather(self, weather_frame=None):
        weather_frame = self.add_weather(weather_frame)
        weather_frame.after(WEATHER_UPDATE_INTERVAL, self.refresh_weather, weather_frame)





