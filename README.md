# Welcome Bach

Get a recording of a random work by Bach on every startup.

## Instalation

1. Clone the repository:

`git clone https://github.com/ofefo/WelcomeBach.git`


2. While in the repository folder, run:

`pip install -r requirements.txt`


3. Edit the **.bashrc** file in */home/etc/* inserting the correct path to **bach.py** at the end of the file:

`sudo python ~/path/to/bach.py`


4. Create a **gnome-terminal.desktop** file inside *~/.config/autostart* with the following:

`[Desktop Entry]
Type=Application
Exec=gnome-terminal
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_NG]=Terminal
Name=Terminal
Comment[en_NG]=Start Terminal On Startup
Comment=Start Terminal On Startup
`