import json
import urllib.request

from globals_radio import *


def read_url_from_file():
    try:
        with open(WEATHER_API_URL_CFG) as f:
            lines = f.readlines()
        return lines[0]
    except IOError:
        return ''


def get_weather():
    try:
        with urllib.request.urlopen(read_url_from_file()) as url:
            data = json.loads(url.read().decode())

            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            if DEBUG:
                print(temp, '°C -', desc)

            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            icon_code = data['weather'][0]['icon']
            weather_text_temp = str(round(temp, 1)) + ' °C'
            weather_text_desc = str(desc)
            return weather_text_temp, weather_text_desc, icon_code

    except Exception as e:
        print(e)
        weather_text_temp = ''
        weather_text_desc = ''
        icon_code = 'error'
        return weather_text_temp, weather_text_desc, icon_code
