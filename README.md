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

1. Clone the repository: `git clone https://github.com/ofefo/welcomeBach.git`

2. Edit the file **gnome-terminal.desktop**, replacing the path to welcomeBach.sh:
*In line 3:*
`Exec=gnome-terminal -- bash -c "home/user/path/to/welcomeBach/welcomeBach.sh"`

3. Then run: `sh setup.sh`

And it's done!

PS: Make sure you have the */autostart* folder! If you don't, create it before step 3 with: `cd ~/.config && mkdir autostart`

This method only works with GNOME.

### Installation for non-GNOME DMs

If GNOME isn't your currently Desktop Manager, you can still run the script as a cli command.

To do it, open the file *Bach* and set the path to your local repository in the DIR variable.

After that, run `sh setup_bin.sh`, and now you can get your daily dose of counterpoint with:

`Bach`


Inspired by [Koan].

[Koan]: https://github.com/a-moreira/Koan
