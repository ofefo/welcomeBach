# welcomeBach

Receive a list of recordings for a random piece by Bach on startup.

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


2. Edit **gnome-terminal.desktop**, replacing the path to welcomeBach.sh:

*In line 3:*
`Exec=path/to/welcomeBach/welcomeBach.sh`

3. Then run:

`bash setup.sh`

And it's done!

Make sure you have the */autostart* folder! If you don't, create it before step 3 with:

`cd ~/.config && mkdir autostart`

Currently only working with GNOME.\
Inspired by [Koan].

[Koan]: https://github.com/a-moreira/Koan
