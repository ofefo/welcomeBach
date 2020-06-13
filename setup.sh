#!/bin/bash

python3 -m venv venv;
dir=$PWD/venv/bin;
. .$dir/activate;
pip3 install -r requirements.txt;
deactivate;
chmod +x "welcomeBach.sh";
cp gnome-terminal.desktop $HOME/.config/autostart/welcomeBach.desktop;
