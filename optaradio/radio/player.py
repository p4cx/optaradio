import os
import re
import struct

import vlc
import socket

try:
    import urllib2
except ImportError:
    import urllib.request as urllib2

HOST_UP = True if os.system('ping -c 1 google.com') is 0 else False

instance = vlc.Instance('--input-repeat=-1')
vlc_player = instance.media_player_new()


def change_station(url):
    if HOST_UP:
        if check_url(url):
            stream = instance.media_new(url)
            vlc_player.set_media(stream)
            vlc_player.play()
            return True
    return False


def stop():
    vlc_player.stop()


def check_url(url, timeout=3):
    try:
        return urllib2.urlopen(url, timeout=timeout).getcode() == 200
    except urllib2.URLError as e:
        print(e)
        return False
    except socket.timeout as e:
        print(e)
        return False


def get_song(url):
    if HOST_UP and check_url(url):
        encoding = 'iso-8859-1'  # default: iso-8859-1 for mp3 and utf-8 for ogg streams
        request = urllib2.Request(url, headers={'Icy-MetaData': 1})  # request metadata
        response = urllib2.urlopen(request)
        meta_int = int(response.headers['icy-metaint'])
        response.read(meta_int)
        metadata_length = struct.unpack('B', response.read(1))[0] * 16
        metadata = response.read(metadata_length).rstrip(b'\0')
        m = re.search(br"StreamTitle='([^']*)';", metadata)
        if m is not None:
            title = m.group(1).decode(encoding, errors='replace')
            return title
    return ''
