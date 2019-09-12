from globals import *

import pygame as pg

from ui.helper import cut_text


def run(window, state):

    def selected_entry(station_):
        if station_[0] is state.play_radio_station:
            playing_icon = pg.image.load(RES_PATH + "icons/playing/playing_big.png")
            window.blit(playing_icon, (70, 280))

            font = pg.font.Font(FONT_SEMIBOLD_PATH, 75)
            station_text = font.render(station_[1].upper(), True, WHITE)
            window.blit(station_text, (130, 250))
        else:
            font = pg.font.Font(FONT_SEMIBOLD_PATH, 75)
            station_text = font.render(station_[1].upper(), True, WHITE)
            window.blit(station_text, (70, 250))

        flag_icon = pg.image.load(RES_PATH + "flags/" + station_[5] + ".png")
        window.blit(flag_icon, (30, 335))
        for num_, line in enumerate(station_[3], start=0):
            font = pg.font.Font(FONT_REGULAR_PATH, 25)
            text = font.render(line, True, WHITE)
            window.blit(text, (100, 340 + (num_ * 30)))

        return len(station_[3])

    def unselected_entry(station_, count, selected_description_length_):
        if count < 0:
            y = 230 + (55 * count)
        else:
            y = 360 + selected_description_length_ * 25 + (55 * count)

        if abs(count) is 1:
            color = [204, 204, 204]
        elif abs(count) is 2:
            color = [153, 153, 153]
        elif abs(count) is 3:
            color = [103, 103, 103]
        elif abs(count) is 4:
            color = [69, 69, 69]
        else:
            color = [51, 51, 51]

        station_name = cut_text.get_first_line(station_[1].upper(), pg.font.Font(FONT_REGULAR_PATH, 40), WINDOW_WIDTH - 120)
        if station_[0] is state.play_radio_station:
            if count > 4 or count < -4:
                count = 5
            playing_icon = pg.image.load(RES_PATH + "icons/playing/playing" + str(abs(count)) + ".png")
            window.blit(playing_icon, (70, y + 12))

            font = pg.font.Font(FONT_SEMIBOLD_PATH, 40)
            station_text = font.render(station_name.upper(), True, color)
            window.blit(station_text, (110, y))
        else:
            font = pg.font.Font(FONT_SEMIBOLD_PATH, 40)
            station_text = font.render(station_name.upper(), True, color)
            window.blit(station_text, (70, y))

    window.fill(BLACK)

    selected_description_length = selected_entry(state.radio_stations[state.selected_radio_station_menu_ui])
    menu_down, menu_up = [], []

    for station in state.radio_stations[state.selected_radio_station_menu_ui + 1:]:
        menu_down.append(station)
    while len(menu_down) < 4:
        for station in state.radio_stations:
            menu_down.append(station)

    for station in reversed(state.radio_stations[:state.selected_radio_station_menu_ui]):
        menu_up.append(station)
    while len(menu_up) < 5:
        for station in reversed(state.radio_stations):
            menu_up.append(station)

    for num, station in enumerate(menu_down, start=1):
        unselected_entry(station, num, selected_description_length)

    for num, station in enumerate(menu_up, start=1):
        unselected_entry(station, -num, selected_description_length)

    pg.display.flip()



