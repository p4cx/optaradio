import sys

import RPi.GPIO as GPIO
import pygame as pg

from ui.input import control

GPIO.setmode(GPIO.BCM)

# rotary encoder
ROTARY_CLK = 5
ROTARY_DT = 6
ROTARY_BUTTON = 13

ROTARY_DIR = True
ROTARY_COUNT = 0
ROTARY_CLK_LAST = 0
ROTARY_CLK_ACTUAL = 0
ROTARY_DELAY = 0.005


SETTING_BUTTON_1 = 2
SETTING_BUTTON_2 = 3
SETTING_BUTTON_3 = 4


def setup(window, state):
    global ROTARY_CLK_LAST
    GPIO.setup(ROTARY_CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ROTARY_DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ROTARY_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    ROTARY_CLK_LAST = GPIO.input(ROTARY_CLK)
    GPIO.add_event_detect(ROTARY_CLK, GPIO.BOTH, callback=rotary_change(window, state), bouncetime=50)
    GPIO.add_event_detect(ROTARY_BUTTON, GPIO.FALLING, callback=control.central_button(window, state), bouncetime=1000)

    GPIO.setup(SETTING_BUTTON_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(SETTING_BUTTON_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(SETTING_BUTTON_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(SETTING_BUTTON_1, GPIO.RISING, callback=control.scroll_menu_up(window, state))
    GPIO.add_event_detect(SETTING_BUTTON_2, GPIO.RISING, callback=control.scroll_menu_down(window, state))
    GPIO.add_event_detect(SETTING_BUTTON_3, GPIO.RISING, callback=close())


def close():
        pg.quit()
        GPIO.cleanup()
        sys.exit()


def rotary_change(window, state):
    ROTARY_CLK_ACTUAL = GPIO.input(ROTARY_CLK)

    if ROTARY_CLK_ACTUAL != ROTARY_CLK_LAST:

        if GPIO.input(ROTARY_DT) != ROTARY_CLK_ACTUAL:
            control.scroll_menu_down(window, state)
        else:
            control.scroll_menu_up(window, state)





