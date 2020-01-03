#!/bin/bash

cd /home/pi
sudo apt-get update
sudo apt-get install imagemagick vlc python3 python3-pip libsdl1.2-dev -y
sudo pip3 install -r ./optaradio/requirements.txt