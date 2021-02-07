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
ROTARY_CLK_LAST = 0
ROTARY_CLK_ACTUAL = 0
ROTARY_DELAY = 0.005

SETTING_BUTTON_1 = 0
SETTING_BUTTON_2 = 3
SETTING_BUTTON_3 = 4


def setup():
    GPIO.setup(ROTARY_CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ROTARY_DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ROTARY_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.setup(SETTING_BUTTON_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(SETTING_BUTTON_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(SETTING_BUTTON_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    print("gpio setup")


def rotary_change(window, state):
    ROTARY_CLK_ACTUAL = GPIO.input(ROTARY_CLK)

    if ROTARY_CLK_ACTUAL != ROTARY_CLK_LAST:

        if GPIO.input(ROTARY_DT) != ROTARY_CLK_ACTUAL:
            control.scroll_menu_down(window, state)
        else:
            control.scroll_menu_up(window, state)


def check_gpio_events(window, state):
    def close():
            pg.quit()
            GPIO.cleanup()
            sys.exit()

    ROTARY_CLK_LAST = GPIO.input(ROTARY_CLK)
    GPIO.add_event_detect(ROTARY_CLK, GPIO.BOTH, callback=lambda w, x: rotary_change(window, state), bouncetime=50)
    GPIO.add_event_detect(ROTARY_BUTTON, GPIO.FALLING, callback=lambda w, x: control.central_button(window, state),
                          bouncetime=1000)

    GPIO.add_event_detect(SETTING_BUTTON_1, GPIO.RISING, callback=lambda w, x: control.scroll_menu_up(window, state))
    GPIO.add_event_detect(SETTING_BUTTON_2, GPIO.RISING, callback=lambda w, x: control.scroll_menu_down(window, state))
    GPIO.add_event_detect(SETTING_BUTTON_3, GPIO.RISING, callback=close())

    if GPIO.event_detected(SETTING_BUTTON_1):
        print('Button pressed')










