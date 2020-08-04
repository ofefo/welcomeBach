#!/bin/bash

if [ -d "$HOME/.local/bin" ]; then
	EXE_PATH=$HOME/.local/bin
else
	EXE_PATH=/usr/local/bin
fi
mkdir -p $EXE_PATH
sed "s|<PWD>|"${PWD}"|" ${PWD}/Bach > $EXE_PATH"/Bach"
chmod +x $EXE_PATH"/Bach"
if [ $1="gnome" ]; then
    mkdir -p $HOME/.config/autostart
    cp welcomeBach.desktop $HOME/.config/autostart/welcomeBach.desktop
fi
