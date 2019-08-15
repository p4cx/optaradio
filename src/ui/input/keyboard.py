import src.radio.main as main


def bind_keys(window, state):
    window.bind('<Return>', lambda event, win=window, s=state: change_to_new_ui(win, s))
    window.bind('<Up>', lambda event, win=window, s=state: scroll_menu_up(win, s))
    window.bind('<Down>', lambda event, win=window, s=state: scroll_menu_down(win, s))
    window.bind('p', lambda event, win=window, s=state: play_radio(win, s))
    window.bind('o', lambda event, win=window, s=state: stop_radio(win, s))



def change_to_new_ui(window, state):
    if state.actual_ui is "start_ui":
        main.change_ui(window, state, "menu_ui")
    else:
        main.change_ui(window, state, "start_ui")


def scroll_menu_up(window, state):
    state.set_selected_radio_station(state, -1)
    main.change_ui(window, state, "menu_ui")


def scroll_menu_down(window, state):
    state.set_selected_radio_station(state, 1)
    main.change_ui(window, state, "menu_ui")


def play_radio(window, state):
    state.play_radio_station = state.selected_radio_station
    main.play(state)
    main.change_ui(window, state, "play_ui")


def stop_radio(window, state):
    state.play_radio_station = -1
    main.stop()
    main.change_ui(window, state, "menu_ui")
