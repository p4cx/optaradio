import os
import re
import struct

import vlc

try:
    import urllib2
except ImportError:
    import urllib.request as urllib2

HOST_UP = True if os.system('ping -c 1 google.com') is 0 else False

instance = vlc.Instance('--input-repeat=-1')
vlc_player = instance.media_player_new()


def change_station(url):
    print(url)
    if HOST_UP:
        stream = instance.media_new(url)
        stream.get_mrl()
        vlc_player.set_media(stream)
        vlc_player.play()
        print(vlc_player.get_media().get_meta(vlc.Meta.NowPlaying))


def stop():
    vlc_player.stop()


def get_song(url):
    if HOST_UP:
        encoding = 'latin1'  # default: iso-8859-1 for mp3 and utf-8 for ogg streams
        request = urllib2.Request(url, headers={'Icy-MetaData': 1})  # request metadata
        response = urllib2.urlopen(request)
        metaint = int(response.headers['icy-metaint'])
        title = ""
        for _ in range(10):  # # title may be empty initially, try several times
            response.read(metaint)  # skip to metadata
            metadata_length = struct.unpack('B', response.read(1))[0] * 16  # length byte
            metadata = response.read(metadata_length).rstrip(b'\0')
            # extract title from the metadata
            m = re.search(br"StreamTitle='([^']*)';", metadata)
            if m:
                title = m.group(1)
                if title:
                    title = title.decode(encoding, errors='replace')
                    break
        return str(title)
