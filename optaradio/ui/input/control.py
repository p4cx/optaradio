from radio import main


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
    elif state.actual_ui is "setting_ui":
        main.switch_setting(state)
        main.change_ui(window, state, "setting_ui")


def back(window, state):
    if state.actual_ui is "menu_ui":
        if state.play_radio_station is -1:
            main.change_ui(window, state, "start_ui")
        else:
            main.stop(state)
    elif state.actual_ui is "setting_ui":
        main.change_ui(window, state, "menu_ui")
    elif state.actual_ui is "play_ui":
        main.stop(state)
        main.change_ui(window, state, "menu_ui")
    else:
        main.change_ui(window, state, "start_ui")


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


def switch_led(window, state):
    main.set_led(window, state)


def switch_audio(window, state):
    main.set_audio(window, state)
