# Welcome Bach

Receive a list of different recordings for a random work by Bach on every startup.

## Installation

1. Clone the repository:

`git clone https://github.com/ofefo/WelcomeBach.git`


2. While in the repository folder, install the requirements with:

`pip install -r requirements.txt`

3. Edit **gnome-terminal.desktop**, replacing the path to bach.py:

*In line 3:*
`Exec=gnome-terminal -- bash -c "cd path/to/welcomeBach && python3 bach.py; cd; exec bash"`


4. Move **gnome-terminal.desktop** to *~/.config/autostart/* with the following:

`sudo cp gnome-terminal.desktop ~/.config/autostart/`


Currently only working in Ubuntu 18.04 with GNOME.
