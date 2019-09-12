import csv
from globals import *


# structure of the csv-file
# id;name;url;description;cover


def get_station_list():
    reader = csv.reader(open(RADIO_STATION_CSV_PATH, newline='', encoding='utf-8'), delimiter=';')
    station_list = []
    for row in reader:
        station_list.append(row)
    reader = csv.reader(open(UNICODE_FLAG_LIST, newline='', encoding='utf-8'), delimiter=';')
    flag_list = []
    for row in reader:
        flag_list.append(row)

    sorted_station_list = sort_station_list(station_list)
    counter = 0
    for num, station in enumerate(sorted_station_list):
        station[0] = counter
        counter += 1
        for country in flag_list:
            if station[5] == country[1]:
                sorted_station_list[num][5] = country[0]
    return sorted_station_list


def sort_station_list(station_list):
    return sorted(station_list, key=lambda x: x[1])
