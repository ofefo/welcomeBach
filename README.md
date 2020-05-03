# welcomeBach

Receive a list of different recordings for a random work by Bach as YouTube links on every startup.

```
Today's Bach is: 
  BWV 1079 – Musikalisches Opfer (The Musical Offering)

https://www.youtube.com/watch?v=rN2p3NgqWos
https://www.youtube.com/watch?v=23yNGer9Wqs
https://www.youtube.com/watch?v=AzT_elDRLJM
```


### Installation

1. Clone the repository:

`git clone https://github.com/ofefo/welcomeBach.git`


2. While in the repository folder, install the requirements with:

`pip install -r requirements.txt`

3. Edit **gnome-terminal.desktop**, replacing the path to bach.py:

*In line 3:*
`Exec=gnome-terminal -- bash -c "cd path/to/welcomeBach && python3 bach.py; cd; exec bash"`


4. Move **gnome-terminal.desktop** to *~/.config/autostart/* with the following:

`sudo cp gnome-terminal.desktop ~/.config/autostart`

Make sure you have the */autostart* folder! If you don't, create it before step 4 with:

`cd ~/.config && mkdir autostart'


Currently only working in Ubuntu 18.04 with GNOME.\
Inspired by [welcomeKoans].

[welcomeKoans]: https://github.com/a-moreira/welcomeKoans
