import os

DEBUG = True

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 600

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
WINDOW_FULL_SCREEN = True

WEATHER_UPDATE_INTERVAL = 60000
WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/weather?lat=48.17967085&lon=11.55411166&APPID=4bb9affe7b5f3e03e75eab31d6bd53f0&units=metric&&lang=en'

TIME_UPDATE_INTERVAL = 1000
SONG_UPDATE_INTERVAL = 2500


RES_PATH = os.getcwd() + '/res/'
SETTINGS_PATH = RES_PATH + 'settings.json'
THUMBS_PATH = RES_PATH + 'radio_thumbs/'
APP_ICON = RES_PATH + 'icons/app_icon.png'
RADIO_STATION_CSV_PATH = RES_PATH + 'radio.csv'

UNICODE_FLAG_FILE = RES_PATH + 'emoji-test.txt'
UNICODE_FLAG_LIST = RES_PATH + 'flag.csv'

FONT_REGULAR_PATH = RES_PATH + 'SourceSansPro-Regular.ttf'
FONT_SEMIBOLD_PATH = RES_PATH + 'SourceSansPro-Semibold.ttf'
