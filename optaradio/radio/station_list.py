import csv

from globals_radio import *


# structure of the csv-file
# id;name;url;description;cover-image;nation
# 2;Groove Salad;http://ice1.somafm.com/groovesalad-256-mp3;A nicely chilled plate of ambient/downtempo beats and
# grooves.;groove_salad.png;United States


def get_station_list():
    reader = csv.reader(open(RADIO_STATION_CSV_PATH, newline='', encoding='utf-8'), delimiter=';')
    station_list = []
    for row in reader:
        station_list.append(row)
        print(row)
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
    print(station_list)
    return sorted_station_list


def sort_station_list(station_list):
    if len(station_list) > 1:
        return sorted(station_list, key=lambda x: x[1])
    else:
        return station_list
