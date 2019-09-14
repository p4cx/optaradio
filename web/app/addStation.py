import csv
from optaradio.globals import *
from web.globals import *
from PIL import Image, ImageFilter

try:
    import urllib2
except ImportError:
    import urllib.request as urllib2


def add_station(entry, cover_path):
    print(entry['station_name'])
    print(entry['station_url'])
    print(entry['station_description'])
    print(entry['station_country'])

    try:
        code = urllib2.urlopen(entry['station_url']).getcode()
        print(code)
        if not (str(code).startswith('2') or str(code).startswith('3')):
            return False, "Your url is not valid."
    except:
        return False, "Your url is not reachable."

    create_cover_image(entry['station_name'], cover_path)


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
    path = THUMBS_PATH + name + ".png"
    background.save(path)
    print(path)



    #len(csv.reader(open(RADIO_STATION_CSV_PATH, newline='', encoding='utf-8'), delimiter=';'))






    return True, "Yeah, alles gut"
