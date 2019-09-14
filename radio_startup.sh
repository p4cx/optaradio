#!/bin/bash

cd /home/pi/optaradio
python3 ./web/main.py &
export DISPLAY=:0
X -nocursor &
python3 ./optaradio/init.py &

