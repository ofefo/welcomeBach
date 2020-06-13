#!/bin/bash

python3 -m venv venv;
dir=$PWD/venv/bin/activate;
. $dir;
pip3 install -r requirements.txt;
deactivate;
chmod +x "Bach";
cp Bach $HOME/.local/bin/;
