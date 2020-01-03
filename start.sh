#!/bin/bash

cd /home/pi/
python3 ./optaradio/web/main.py &
export DISPLAY=:0
X -nocursor &
python3 ./optaradio/optaradio/init.py &

