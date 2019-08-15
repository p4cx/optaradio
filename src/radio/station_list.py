import csv
from src.globals import *


# structure of the csv-file
# id;name;url;description;cover


def get_station_list():
    reader = csv.reader(open(RADIO_STATION_CSV_PATH, newline='', encoding='utf-8'), delimiter=';')
    station_list = []
    for row in reader:
        station_list.append(row)
    sorted_station_list = sort_station_list(station_list)
    counter = 0
    for x in sorted_station_list:
        x[0] = counter
        counter += 1
    return sorted_station_list


def sort_station_list(station_list):
    return sorted(station_list, key=lambda x: x[1])
