from src.globals import *
from src.radio import player

import tkinter as tk


class PlayUI:

    def __init__(self, window, state):
        self.window = window
        self.actual_station(state)
        self.refresh_actual_station_song(state, "")
        self.station_cover(state)

    def actual_station(self, state):
        play_station = tk.Frame(self.window, relief=tk.SOLID, bd=1, bg="#000")
        print(state.radio_stations[state.play_radio_station][1])
        tk.Label(play_station, text=state.radio_stations[state.play_radio_station][1].upper(), bg="#000", font=(FONT_SEMIBOLD, 70), fg='#fff').pack()
        play_station.place(x=50, y=500)

    def add_actual_station_song(self, state, old_song, old_song_frame=None):
        song_frame = tk.Frame(self.window, relief=tk.SOLID, bd=1, bg="#000")
        song = player.get_song(state.radio_stations[state.play_radio_station][2])
        if old_song is not song and len(song) > 2:
            tk.Label(song_frame, text=song, bg="#000", font=(FONT_REGULAR, 30), fg="#fff", padx=10).pack()
            song_frame.place(x=50, y=580)
            old_song = song
        else:
            tk.Label(song_frame, text=old_song, bg="#000", font=(FONT_REGULAR, 30), fg="#fff", padx=10).pack()
            song_frame.place(x=50, y=580)
        if old_song_frame is not None:
            old_song_frame.destroy()

        return old_song, song_frame

    def refresh_actual_station_song(self, state, old_song, song_frame=None):
        old_song, song_frame = self.add_actual_station_song(state, old_song, song_frame)
        song_frame.after(SONG_UPDATE_INTERVAL, self.refresh_actual_station_song, state, old_song, song_frame)

    def station_cover(self, state):
        cover_frame = tk.Frame(self.window, relief=tk.SOLID, bd=1, bg="#000")
        station_cover = tk.PhotoImage(file=RES_PATH + "radio_thumbs/" + state.radio_stations[state.play_radio_station][4])
        station_cover_label = tk.Label(cover_frame, image=station_cover, bg="#000")
        station_cover_label.image = station_cover
        station_cover_label.pack()
        cover_frame.place(x=50, y=50)






