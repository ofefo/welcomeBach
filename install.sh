#!/bin/bash

if [ -d "$HOME/.local/bin" ]; then
	EXE_PATH=$HOME/.local/bin
	SUCCESS=1
else
	if [ "$(whoami)" == "root" ]; then
		echo "Can't install in your home folder! Need permission to do it in /usr/, try again with sudo!"
		exit
	else
		EXE_PATH=/usr/local/bin
		SUCCESS=1
	fi
fi
touch ${PWD}/listened.txt
sed "s|<PWD>|"${PWD}"|" ${PWD}/Bach > $EXE_PATH"/Bach"
chmod +x $EXE_PATH"/Bach"
if [ $1="gnome" ]; then
    mkdir -p $HOME/.config/autostart
    cp welcomeBach.desktop $HOME/.config/autostart/welcomeBach.desktop
fi
if [ $SUCCESS == 1 ]; then
	echo "Done! You're ready to get polyphonic."
fi
