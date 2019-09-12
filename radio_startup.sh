#!/bin/bash

cd /home/pi/optaradio
export DISPLAY=:0
X -nocursor &
python3 ./src/__init__.py &

