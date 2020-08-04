#!/bin/bash

if [ -d "$HOME/.local/bin" ]; then
	EXE_PATH=$HOME/.local/bin
else
	if [[ $EUID > 0 ]]; then
		echo "Can't install in your home folder! Need permission to do it in /usr/, try again with sudo!"
	else
		EXE_PATH=/usr/local/bin
	fi
fi
touch listened.txt
mkdir -p $EXE_PATH
sed "s|<PWD>|"${PWD}"|" ${PWD}/Bach > $EXE_PATH"/Bach"
chmod +x $EXE_PATH"/Bach"
if [ $1="gnome" ]; then
    mkdir -p $HOME/.config/autostart
    cp welcomeBach.desktop $HOME/.config/autostart/welcomeBach.desktop
fi
