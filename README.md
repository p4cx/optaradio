![# optaradio](./web/static/radio_plash.png)   
   
---

##### software and other stuff for my personal internet radio side project
# WORK IN PROGRESS

---

### what have i done:

my dad cleaned up his cellar and found a *Loewe Opta R115* radio there and gave it to me. over a long period of time, i have made and coded something. and that's it.
this repository contains two parts: radio software for raspberry pi and web interface (runs also on the pi) to add, modify, delete, control the radio stations on the raspberry pi.

---

### how i use/make/run that:

you can run the radio software as standalone on your desktop, buts that a bit stupid, because there are way better tools for this task. 

*these instructions require some linux knowledge*


#### prepare 🥧
1. copy [Raspbian Lite](https://www.raspberrypi.org/downloads/raspbian/) on a micro sd card and inserted it in the Raspberry Pi (mine is a 3rd gen., model B, rev 1.2)
2. Run `sudo raspi-config` and ...
    - ... turn SSH on and put a key file on that puppy (because nobody wants to type `raspberry` in over a 1000 times)
    - ... set `Boot Option -> B1 Desktop / CLI` to `B2 Console Autologin`
3. remove boring booting stuff
   - add `disable_splash=1` at the end of `/boot/config.txt` and save
   - add `logo.nologo quiet` and change `console=tty1` to `console=tty3` in `/boot/cmdline.txt` and save
4. run `sudo apt-get update`
5. run  `sudo apt-get install python3-pip python3-dev nginx vlc uwsgi xorg libsdl-ttf2.0-0 pulseaudio`
6. run `pip3 -r install requirements.txt` in the freshly cloned optaradio repo


5. create a crontab for autostart
	- `sudo crontab -e`
	- insert ```@reboot sh /home/pi/optaradio/radio_startup.sh >/home/pi/optaradio/logs/cronlog 2>&1```
6. test it and if it runs: be happy

#### run the 🐍 radio software 
1. install `python3`
2. install `pip3` (if its not already included with your python installation)
3. install `vlc`
4. install `pygame` and `python-vlc` via `pip`
5. drink some ☕️


#### use optaradio
**controls on desktop:**    
- `return`: input   
- `up`: up   
- `down`: down   
- `s`: settings   
- `c`: pause   

#### build 📻
1. get an old radio
2. get rid of all old crap inside
3. put a nice lcd and other fancy electronic stuff inside
4. jump in 🌙 light around the radio
5. squeeze your Raspberry Pi in the housing
6. turn it on and have fun

(ps. good luck 🍀)



