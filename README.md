![# optaradio](./web/static/radio_plash.png)   
   
---

##### software and other stuff for my personal internet radio side project
# WORK IN PROGRESS

---

### what have i done:

My father tidied up his basement and found a *Loewe Opta R115* radio. It worked but had an annoying noise in the background and along with the fact that UKW (FM), "Ultrakurzwelle" will be turned off in the future, I decided to rip out all of the stuff and turn it into an internet radio.   
It took quite a while. But now I reached a step in which the software and hardware is usable!

I try to document everything, so if you want to recreate this (aka. wake up the dragon): Good luck 🍀    
This is no step to step instruction, so you should take your time and think yourself. 

---

### hardware i used 🕹

- Raspberry Pi 3 Model B V1.2
- [1024x600px Display with HDMI](https://de.aliexpress.com/item/32700714288.html)
- cheap USB Soundcard (3.5 plug on RPI is crap)
- Amplifier with TPA3116D2 (have to check it out first, if it works fine)
- Monacor SP-13/4 speaker
- MeanWell RS-75-12 power supply (hope it delivers enough power for everything)

---

### how i use/make/run that:

You can run the radio software as standalone on your desktop, buts that a bit stupid, because there are way better tools to play internet radio on your pc.

#### prepare 🥧
[all commands in your user space: `/home/pi` unless its explicit declared]

1. flash [Raspbian Lite](https://www.raspberrypi.org/downloads/raspbian/) on a micro sd card
2. `touch ssh` in the root dir on the micro sd card
3. connect via ssh and run `raspi-config`
    - System Options > Wireless LAN
    - System Options > Password
    - System Options > Boot / Auto Login > Console Autologin
3. remove boring booting stuff (optional)
   - add `disable_splash=1` at the end of `/boot/config.txt` and save
   - add `logo.nologo quiet` and change `console=tty1` to `console=tty3` in `/boot/cmdline.txt` and save
4. install everything needed
    - `apt update`
    - `apt upgrade`
    - `apt install --no-install-recommends xserver-xorg x11-xserver-utils xinit`    
      (i know, i could use framebuffer with pygame, but I want to grab the pygame window over ssh and therefore I need xserver)   
    - `apt install git python3-pip vlc imagemagick pulseaudio libsdl-ttf2.0-0 python3-rpi.gpio`
5. `dpkg-reconfigure tzdata` and set your correct location for time
6. `git clone https://github.com/p4cx/optaradio.git` in your user directory `/home/pi`
7. run `pip3 -r install requirements.txt` in the freshly cloned optaradio repo
8. grab an api url from [openweathermap](https://openweathermap.org/) and paste it into `nano weater.cfg` - it should look like this: *http://api.openweathermap.org/data/2.5/weather?q=munich&units=metric&appid=1234567890abcdefghijklmnopqrstuv*   
Attention: get sure, that units is metric: "units=metric". 
9. `./optaradio/build.sh` to get fonts and emojis from external repositorys

-- have to test this   

8. create a crontab for autostart
	- `sudo crontab -e`
	- insert ```@reboot sh /home/pi/optaradio/radio_startup.sh >/home/pi/optaradio/logs/cronlog 2>&1```
9. test it and if it runs: be happy

#### developing 💻

- activate X11 fowarding on your host machine (sshd config)    
`ssh pi@x.x.x.x -Y` on your machine and you will get the pygame window on your desktop
- how do get radiothumbnails on the pi? Copy it manually with filezilla!

#### gpio usage 💡

| USAGE | PIN | PIN | USAGE |
|:---|---:|:---|---:|
| Power for all buttons | __3V3__ | __5V__ | -- |
| Favourite button 1 | __2__ | __5V__ | Power for rotary encoder |
| Favourite button 2 | __3__ | __GND__ | Ground for rotary encoder |
| Favourite button 3 | __4__ | __14__ | Rotary encoder button |
| -- | __GND__ | __15__ | Data channel rotary encoder |
| Favourite button 4 | __17__ | __18__ | Clock rotary encoder |
| Favourite button 5 | __27__ | __GND__ | Ground for relais |
| Favourite button 6 | __22__ | __23__ | Channel 1 for relais |
| -- | __3V3__ | __24__ | Channel 2 for relais |
| -- | __10__ | __GND__ | -- |
| Favourite button 7 | __9__ | __25__ | Setting button 1 |
| -- | __11__ | __8__ | Setting button 2 |
| -- | __GND__ | __7__ | Setting button 3 |
| Update button | __0__ | __1__ | Setting button 4 |
| -- | __5__ | __GND__ | -- |
| -- | __6__ | __12__ | -- |
| -- | __13__ | __GND__ | -- |
| -- | __19__ | __16__ | -- |
| -- | __26__ | __20__ | -- |
| -- | __GND__ | __21__ | -- |

#### run the 🐍 radio software 
1. `cd ./optaradio`
2. `python3 ./init.py`

#### control optaradio
basic idea of controlling the radio: Like iDrive from BMW, rotate the wheel (in my case the KY-040 rotary encoder) to go up and down und press it to activate menu entry.   

**control on desktop:**    
- `return`: input  
- `up`: up   
- `down`: down  
- `1`-`7`: Favourite buttons  
- `q`: go back   
- `w`: audio on/off   
- `e`: LED on/off (future project)   
- `r`: settings   
- `ESC`: exit   

**control with real buttons:**    
- look at gpio usage, it should be self explaining

#### build 📻
1. get an old radio
2. get rid of all old crap inside
3. put a nice lcd and other fancy electronic stuff inside
4. jump in 🌙 light around the radio
5. squeeze your Raspberry Pi in the housing
6. turn it on and have fun
