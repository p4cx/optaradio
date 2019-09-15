import csv
from optaradio.globals import *


def get():
    reader = csv.reader(open(RADIO_STATION_CSV_PATH, newline='', encoding='utf-8'), delimiter=';')
    station_list = []
    for row in reader:
        station_list.append(row)
    sorted_station_list = sorted(station_list, key=lambda x: x[1])

    return sorted_station_list

