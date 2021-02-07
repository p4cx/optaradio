#!/bin/bash

# remove old font files, mini.css and emoji-test-txt
rm -f ./optaradio/res/SourceSansPro-Regular.ttf ./optaradio/res/SourceSansPro-Semibold.ttf ./web/static/SourceSansPro-Regular.ttf ./web/static/SourceSansPro-Semibold.ttf ./web/static/SourceSansPro-Regular.woff ./web/static/SourceSansPro-Semibold.woff ./web/static/mini.css ./optaradio/res/flags/*

# clone ttf font files and copy them into the optaradio repo
wget https://github.com/adobe-fonts/source-sans-pro/raw/1cac893f2d6535a2ff45818043985a4e88c1cf70/TTF/SourceSans3-Regular.ttf -O ./optaradio/res/SourceSansPro-Regular.ttf
wget https://github.com/adobe-fonts/source-sans-pro/raw/1cac893f2d6535a2ff45818043985a4e88c1cf70/TTF/SourceSans3-Semibold.ttf -O ./optaradio/res/SourceSansPro-Semibold.ttf

# clone woff font files and copy them into the optaradio repo
wget https://github.com/adobe-fonts/source-sans-pro/raw/1cac893f2d6535a2ff45818043985a4e88c1cf70/WOFF/TTF/SourceSans3-Regular.ttf.woff -O ./web/static/SourceSansPro-Regular.woff
wget https://github.com/adobe-fonts/source-sans-pro/raw/1cac893f2d6535a2ff45818043985a4e88c1cf70/WOFF/TTF/SourceSans3-Semibold.ttf.woff -O ./web/static/SourceSansPro-Semibold.woff

# copy font files to web folder
cp ./optaradio/res/SourceSansPro-Regular.ttf ./web/static/SourceSansPro-Regular.ttf
cp ./optaradio/res/SourceSansPro-Semibold.ttf ./web/static/SourceSansPro-Semibold.ttf 

# get mini.css for web interface
wget https://raw.githubusercontent.com/Chalarangelo/mini.css/534ae81268710951fc4458d28a5813b8708679ba/dist/mini-dark.min.css -O ./web/static/mini.css

# clone flag emojis for radio interface, copy them to right dir and delete openmoji repo
git clone --dept 1 https://github.com/hfg-gmuend/openmoji.git
cp -v ./openmoji/color/72x72/1F1* ./optaradio/res/flags/
cp -v ./openmoji/color/72x72/1F3F3-* ./optaradio/res/flags/rainbow.png
rm -rf ./openmoji

# resize flag size
mogrify -resize 50x50 ./optaradio/res/flags/*.png