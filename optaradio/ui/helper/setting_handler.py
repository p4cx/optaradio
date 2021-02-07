import pygame as pg

import json
import copy

from globals_radio import *
from ui.helper import cut_text


def load_settings_data():
    with open(SETTINGS_PATH, 'r') as settings:
        setting_data = json.load(settings)

    setting_list = list(setting_data.keys())
    for entry in setting_list:
        setting_data[entry]['description'] = cut_text.get_multi_line(
            setting_data[entry]['description'], pg.font.Font(FONT_REGULAR_PATH, 25), WINDOW_WIDTH - 120
        )
    return setting_data


def save_settings_data(state):
    save_setting_data = copy.deepcopy(state.setting_data)
    setting_list = list(save_setting_data.keys())
    for entry in setting_list:
        save_setting_data[entry]['description'] = "".join(save_setting_data[entry]['description'])

    with open(SETTINGS_PATH, 'w') as settings:
        json.dump(save_setting_data, settings)


def set_setting(state, id_):
    if isinstance(id_, int):
        setting_id = list(state.setting_data.keys())[id_]
    else:
        setting_id = id_

    if state.setting_data[setting_id]['status'] == "off":
        state.setting_data[setting_id]['status'] = "on"
    else:
        state.setting_data[setting_id]['status'] = "off"

    save_settings_data(state)
