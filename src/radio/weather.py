import urllib.request
import json
from src.globals import *


def get_weather():
    try:
        with urllib.request.urlopen(WEATHER_API_URL) as url:
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
        weather_text_temp = 'No weather data available'
        weather_text_desc = 'Check your internet connection'
        icon_code = 'error'
        return weather_text_temp, weather_text_desc, icon_code
