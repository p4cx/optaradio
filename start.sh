#!/bin/bash

cd /home/pi/optaradio/optaradio/
#export PYTHONPATH=.
#sudo python3 ./web/main.py &
pulseaudio -D
export DISPLAY=:0
X -nocursor &
python3 ./init.py &

