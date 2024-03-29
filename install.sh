#!/bin/bash

python3 -m venv venv;
. venv/bin/activate;
pip3 install beautifulsoup4;
deactivate;

if [ -d "$HOME/.local/bin" ]; then
	EXE_PATH=$HOME/.local/bin
	SUCCESS=true
else
	if [ ! "$(whoami)" == "root" ]; then
		echo "Can't install in your home folder! Need permission to do it in /usr/, try again with sudo!"
		exit
	else
		EXE_PATH=/usr/local/bin
		SUCCESS=true
	fi
fi
sed "s|<PWD>|"${PWD}"|" ${PWD}/welcomebach/welcomebach > $EXE_PATH"/welcomebach"
chmod +x $EXE_PATH"/welcomebach"
if [ $1="gnome" ]; then
    mkdir -p $HOME/.config/autostart
    cp ./welcomebach/welcomeBach.desktop $HOME/.config/autostart/welcomeBach.desktop
fi
if $SUCCESS; then
	echo "Done! You're ready to get polyphonic."
fi
