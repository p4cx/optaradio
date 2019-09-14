#!/bin/bash

rm -f ./optaradio/res/SourceSansPro-Regular.ttf ./optaradio/res/SourceSansPro-Semibold.ttf ./web/static/SourceSansPro-Regular.ttf ./web/static/SourceSansPro-Semibold.ttf ./web/static/SourceSansPro-Regular.woff ./web/static/SourceSansPro-Semibold.woff ./web/static/mini.css ./web/static/emoji-test.txt

wget -q https://github.com/adobe-fonts/source-sans-pro/raw/release/TTF/SourceSansPro-Regular.ttf -O ./optaradio/res/SourceSansPro-Regular.ttf
wget https://github.com/adobe-fonts/source-sans-pro/raw/release/TTF/SourceSansPro-Semibold.ttf -O ./optaradio/res/SourceSansPro-Semibold.ttf

wget -q https://github.com/adobe-fonts/source-sans-pro/raw/release/WOFF/TTF/SourceSansPro-Regular.ttf.woff -O ./web/static/SourceSansPro-Semibold.woff
wget -q https://github.com/adobe-fonts/source-sans-pro/raw/release/WOFF/TTF/SourceSansPro-Semibold.ttf.woff -O ./web/static/SourceSansPro-Regular.woff

cp ./optaradio/res/SourceSansPro-Regular.ttf ./web/static/SourceSansPro-Regular.ttf
cp ./optaradio/res/SourceSansPro-Semibold.ttf ./web/static/SourceSansPro-Semibold.ttf 

wget https://raw.githubusercontent.com/Chalarangelo/mini.css/master/dist/mini-dark.min.css -O ./web/static/mini.css

wget -q https://unicode.org/Public/emoji/12.0/emoji-test.txt -O ./web/static/emoji-test.txt

