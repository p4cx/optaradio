#!/bin/bash

rsync -r -a -v -e "ssh -l pi" --delete ./* 10.42.0.20:/home/pi/optaradio/
ssh pi@10.42.0.20 << EOF
sudo chmod +x /home/pi/optaradio/radio_startup.sh
mkdir -p /home/pi/optaradio/logs
sudo reboot -h
EOF