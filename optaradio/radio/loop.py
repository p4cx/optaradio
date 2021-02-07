import pygame as pg

from radio import main
from ui.input import keyboard


def run_loop(window, state):
    old_ticks = 0
    tick_count = 1
    ground_tick = 500  # 0.5s update heart beat
    rotary_clk_last = 0

    try:
        import RPi.GPIO
        from ui.input import gpio

        gpio_available = True
    except ImportError:
        gpio_available = False

    if gpio_available:
        gpio.setup()

    while True:
        keyboard.check_keyboard_events(window, state)

        if gpio_available:
            rotary_clk_last = gpio.check_gpio_events(window, state, rotary_clk_last)

        actual_ticks = pg.time.get_ticks()
        delta_ticks = (actual_ticks - old_ticks)

        if delta_ticks > ground_tick:
            tick_count += 1
            old_ticks = actual_ticks

            # start_ui
            if state.actual_ui == "start_ui":
                main.update_ui(window, state, "clock")
                if tick_count % 120 is 0:
                    main.update_ui(window, state, "weather")
            elif state.actual_ui == "play_ui":
                if len(state.actual_playing_song) is "":
                    main.update_ui(window, state, "")
                if tick_count % 10 is 0:
                    main.update_ui(window, state, "")

        pg.time.wait(0)
