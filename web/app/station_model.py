import os
import csv
from optaradio.globals import *
from web.globals import *
from PIL import Image, ImageFilter

try:
    import urllib2
except ImportError:
    import urllib.request as urllib2


def get():
    reader = csv.reader(open(RADIO_STATION_CSV_PATH, newline='', encoding='utf-8'), delimiter=';')
    station_list = []
    for row in reader:
        station_list.append(row)
    sorted_station_list = sort_station_list(station_list)

    return sorted_station_list


def sort_station_list(station_list):
    if len(station_list) > 1:
        return sorted(station_list, key=lambda x: x[1])
    else:
        return station_list


def add(entry, cover_path):
    print(entry['station_name'])
    print(entry['station_url'])
    print(entry['station_desc'])
    print(entry['station_country'])

    station_list = get()

    for station in station_list:
        if station[1] == entry['station_name']:
            return False, "Your choosen name is already taken.", []

    try:
        code = urllib2.urlopen(entry['station_url']).getcode()
        print(code)
        if not (str(code).startswith('2') or str(code).startswith('3')):
            return False, "Your url is not valid.", []
    except:
        return False, "Your url is not reachable.", []

    path, image_file = create_cover_image(entry['station_name'], cover_path)
    write_to_csv(entry['station_name'], entry['station_url'], entry['station_description'], image_file, entry['station_country'], "add")

    return True, "Added " + entry['station_name'] + " to your station list.", [entry['station_name'], entry['station_url'], entry['station_description'], path, entry['station_country']]


def create_cover_image(name, cover_path):
    cover = Image.open(cover_path).convert('RGBA')
    c_width, c_height = cover.size
    if c_width is not 400 or c_height is not 400:
        cover_resize = cover.resize((400, 400), Image.ANTIALIAS)
    else:
        cover_resize = cover.copy
    blur_layer = Image.open(STATIC_PATH + "blur_layer.png").convert('RGBA')
    background = Image.open(cover_path).convert('RGBA')
    background_resize = background.resize((1024, 500), Image.ANTIALIAS)
    background_blur = background_resize.filter(ImageFilter.GaussianBlur(75))
    background = Image.alpha_composite(background_blur, blur_layer)
    background.paste(cover_resize, (312, 50))
    file = name + ".png"
    path = THUMBS_PATH + file
    background.save(path)
    return "/image/" + file, file


def write_to_csv(name, url, description, file, country, add_mod_del, old_name=None):
    reader = csv.reader(open(RADIO_STATION_CSV_PATH, newline='', encoding='utf-8'), delimiter=';')
    station_list = []
    try:
        for row in reader:
            if add_mod_del == "mod" and row[1] == old_name:
                if "/" in file:
                    path, file = create_cover_image(name, file)
                row = [row[0], name, url, description, file, country]
                station_list.append(row)
                print("modify", row)
            elif add_mod_del == "del" and row[1] == name:
                print("delete", row)
            else:
                station_list.append(row)
        if add_mod_del == "add":
            row = [station_list[-1][0] + 1, name, url, description, file, country]
            station_list.append(row)
            print("add", row)
        with open(RADIO_STATION_CSV_PATH, 'w') as csvFile:
            writer = csv.writer(csvFile, delimiter=';')
            writer.writerows(station_list)
        csvFile.close()
        print("yeah")
        return True, "Yeah", [name, url, description, file, country]
    except Exception as e:
        print(e)
        return False, "Upps" + str(e), [name, url, description, file, country]


def crawl_station_list(station_name):
    stations_list = get()
    print(stations_list)
    for station in stations_list:
        if station_name == station[1]:
            print(station)
            return station
    return None


def modify_station(entry, file_name, old_name):
    print(entry['station_name'])
    print(entry['station_url'])
    print(entry['station_desc'])
    print(entry['station_country'])
    print(file_name)
    print(old_name)
    return write_to_csv(entry['station_name'], entry['station_url'], entry['station_desc'], file_name, entry['station_country'], "mod", old_name)


def delete_station(name):
    station = crawl_station_list(name)
    return write_to_csv(station[1], station[2], station[3], station[4], station[5], "del")
