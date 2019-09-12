import vlc
import os
import re
import struct

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


def stop():
    vlc_player.stop()


def get_song(url):
    if HOST_UP:
        request = urllib2.Request(url, headers={'Icy-MetaData': 1})
        response = urllib2.urlopen(request)
        meta_int = int(response.headers['icy-metaint'])
        output = ''
        response.read(meta_int)
        metadata_length = struct.unpack('B', response.read(1))[0] * 16
        metadata = response.read(metadata_length).rstrip(b'\0')
        m = re.search(br"StreamTitle='([^']*)';", metadata)
        if m:
            title = m.group(1)
            if title:
                search = '\''
                song = str(title)
                pos_a = song.find(search)
                check = True
                if pos_a == -1:
                    check = False
                pos_b = song.rfind(search)
                if pos_b == -1:
                    check = False
                adjusted_pos_a = pos_a + 1
                if adjusted_pos_a >= pos_b:
                    check = False
                if check:
                    output = str(song[adjusted_pos_a:pos_b])
        return output

