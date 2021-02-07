import pygame as pg

from globals_radio import *
from ui.helper import cut_text
from ui import bar


def run(window, state):
    def selected_entry(entry_):
        if entry_['status'] == "on":
            playing_icon = pg.image.load(RES_PATH + "icons/toggle/on.png")
        else:
            playing_icon = pg.image.load(RES_PATH + "icons/toggle/off.png")
        window.blit(playing_icon, (70, 280))
        font = pg.font.Font(FONT_SEMIBOLD_PATH, 75)
        setting_text = font.render(entry_['title'].upper(), True, WHITE)
        window.blit(setting_text, (150, 250))
        for num_, line in enumerate(entry_['description'], start=0):
            font = pg.font.Font(FONT_REGULAR_PATH, 25)
            text = font.render(line, True, WHITE)
            window.blit(text, (100, 340 + (num_ * 30)))

        return len(entry_['description'])

    def unselected_entry(entry_, count, selected_description_length_):
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

        setting_name = cut_text.get_first_line(entry_['title'].upper(), pg.font.Font(FONT_REGULAR_PATH, 40),
                                               WINDOW_WIDTH - 120)
        font = pg.font.Font(FONT_SEMIBOLD_PATH, 40)
        setting_text = font.render(setting_name.upper(), True, color)
        window.blit(setting_text, (70, y))

    window.fill(BLACK)

    setting_list = list(state.setting_data.keys())

    selected_description_length = selected_entry(state.setting_data[setting_list[state.selected_entry_setting_ui]])
    menu_down, menu_up = [], []

    for entry in setting_list[state.selected_entry_setting_ui + 1:]:
        menu_down.append(entry)
    while len(menu_down) < 4:
        for entry in setting_list:
            menu_down.append(entry)

    for entry in reversed(setting_list[:state.selected_entry_setting_ui]):
        menu_up.append(entry)
    while len(menu_up) < 5:
        for entry in reversed(setting_list):
            menu_up.append(entry)

    for num, entry in enumerate(menu_down, start=1):
        unselected_entry(state.setting_data[entry], num, selected_description_length)

    for num, entry in enumerate(menu_up, start=1):
        unselected_entry(state.setting_data[entry], -num, selected_description_length)

    if state.setting_data['show_buttons']['status'] == "on":
        bar.add_bar(window, state)

    pg.display.flip()
