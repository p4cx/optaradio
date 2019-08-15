import os

DEBUG = True
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 700
WINDOW_FULL_SCREEN = False
WEATHER_UPDATE_INTERVAL = 60000
TIME_UPDATE_INTERVAL = 1000
SONG_UPDATE_INTERVAL = 2500
RES_PATH = os.getcwd() + '/res/'
RADIO_STATION_CSV_PATH = RES_PATH + 'radio.csv' # csv file with all radio stations in /res folder
FONT_REGULAR = 'SourceSansPro-Regular'
FONT_SEMIBOLD = 'SourceSansPro-Semibold'
WEATHER_API_URL = 'https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22' # valid link to api by openweathermap.org