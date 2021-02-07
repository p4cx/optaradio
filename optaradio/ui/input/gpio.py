import sys

import RPi.GPIO as GPIO
import pygame as pg

from ui.input import control

GPIO.setmode(GPIO.BCM)

# rotary encoder
ROTARY_CLK = 18
ROTARY_DT = 15
ROTARY_BUTTON = 14

ROTARY_DIR = True
ROTARY_COUNT = 0
ROTARY_CLK_ACTUAL = 0
ROTARY_DELAY = 0.005

SETTING_BUTTON_1 = 25
SETTING_BUTTON_2 = 8
SETTING_BUTTON_3 = 7
SETTING_BUTTON_4 = 1

FAVOURITE_BUTTON_1 = 2
FAVOURITE_BUTTON_2 = 3
FAVOURITE_BUTTON_3 = 4
FAVOURITE_BUTTON_4 = 17
FAVOURITE_BUTTON_5 = 27
FAVOURITE_BUTTON_6 = 22
FAVOURITE_BUTTON_7 = 9

UPDATE_BUTTON = 0


def setup():
    GPIO.setup(ROTARY_CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ROTARY_DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ROTARY_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(ROTARY_CLK, GPIO.BOTH, bouncetime=50)
    GPIO.add_event_detect(ROTARY_BUTTON, GPIO.FALLING, bouncetime=200)

    GPIO.setup(SETTING_BUTTON_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(SETTING_BUTTON_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(SETTING_BUTTON_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(SETTING_BUTTON_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(SETTING_BUTTON_1, GPIO.RISING, bouncetime=200)
    GPIO.add_event_detect(SETTING_BUTTON_2, GPIO.RISING, bouncetime=200)
    GPIO.add_event_detect(SETTING_BUTTON_3, GPIO.RISING, bouncetime=200)
    GPIO.add_event_detect(SETTING_BUTTON_4, GPIO.RISING, bouncetime=200)

    GPIO.setup(FAVOURITE_BUTTON_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(FAVOURITE_BUTTON_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(FAVOURITE_BUTTON_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(FAVOURITE_BUTTON_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(FAVOURITE_BUTTON_5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(FAVOURITE_BUTTON_6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(FAVOURITE_BUTTON_7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(FAVOURITE_BUTTON_1, GPIO.RISING, bouncetime=200)
    GPIO.add_event_detect(FAVOURITE_BUTTON_2, GPIO.RISING, bouncetime=200)
    GPIO.add_event_detect(FAVOURITE_BUTTON_3, GPIO.RISING, bouncetime=200)
    GPIO.add_event_detect(FAVOURITE_BUTTON_4, GPIO.RISING, bouncetime=200)
    GPIO.add_event_detect(FAVOURITE_BUTTON_5, GPIO.RISING, bouncetime=200)
    GPIO.add_event_detect(FAVOURITE_BUTTON_6, GPIO.RISING, bouncetime=200)
    GPIO.add_event_detect(FAVOURITE_BUTTON_7, GPIO.RISING, bouncetime=200)

    GPIO.setup(UPDATE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(UPDATE_BUTTON, GPIO.RISING, bouncetime=200)


def rotary_change(window, state, rotary_clk_last):

    if GPIO.input(ROTARY_CLK) != rotary_clk_last:

        if GPIO.input(ROTARY_DT) != ROTARY_CLK_ACTUAL:
            control.scroll_menu_down(window, state)
        else:
            control.scroll_menu_up(window, state)

    return GPIO.input(ROTARY_CLK)


def check_gpio_events(window, state, rotary_clk_last):
    def close():
        pg.quit()
        GPIO.cleanup()
        sys.exit()

    events = pg.event.get()

    for event in events:
        if event.type == pg.QUIT:
            close()

    if GPIO.event_detected(ROTARY_BUTTON):
        control.central_button(window, state)

    if GPIO.event_detected(ROTARY_CLK):
        return rotary_change(window, state, rotary_clk_last)

    if GPIO.event_detected(SETTING_BUTTON_1):
        control.back(window, state)
    elif GPIO.event_detected(SETTING_BUTTON_2):
        control.switch_audio(window, state)
    elif GPIO.event_detected(SETTING_BUTTON_3):
        control.switch_led(window, state)
    elif GPIO.event_detected(SETTING_BUTTON_4):
        control.open_setting(window, state)

    if GPIO.event_detected(FAVOURITE_BUTTON_1):
        control.play_favourite(window, state, 1)
    elif GPIO.event_detected(FAVOURITE_BUTTON_2):
        control.play_favourite(window, state, 2)
    elif GPIO.event_detected(FAVOURITE_BUTTON_3):
        control.play_favourite(window, state, 3)
    elif GPIO.event_detected(FAVOURITE_BUTTON_4):
        control.play_favourite(window, state, 4)
    elif GPIO.event_detected(FAVOURITE_BUTTON_5):
        control.play_favourite(window, state, 5)
    elif GPIO.event_detected(FAVOURITE_BUTTON_6):
        control.play_favourite(window, state, 6)
    elif GPIO.event_detected(FAVOURITE_BUTTON_7):
        control.play_favourite(window, state, 7)

    if GPIO.event_detected(UPDATE_BUTTON):
        print("update")




