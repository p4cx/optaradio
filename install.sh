#!/bin/bash

cd /home/pi
sudo apt-get update
sudo cp /etc/apt/sources.list /etc/apt/sources.list~
sudo sed -Ei 's/^# deb-src /deb-src /' /etc/apt/sources.list
sudo sed -Ei 's/^#deb-src /deb-src /' /etc/apt/sources.list
sudo apt-get update
sudo apt-get install imagemagick vlc python3 python3-pip -y
sudo apt-get build-dep python-pygame -y
sudo pip3 install -r ./optaradio/requirements.txt