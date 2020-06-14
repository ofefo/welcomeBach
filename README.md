# welcomeBach

Receive a list of YouTube links to recordings of a randomly selected piece by Bach on startup.

```
Today's Bach is: 
  BWV 1079 – Musikalisches Opfer (The Musical Offering)

https://www.youtube.com/watch?v=rN2p3NgqWos
https://www.youtube.com/watch?v=23yNGer9Wqs
https://www.youtube.com/watch?v=AzT_elDRLJM
```


### Installation

1. Clone the repository: `git clone https://github.com/ofefo/welcomeBach.git`

2. Edit the file **welcomeBach.desktop**, replacing the path to welcomeBach.sh *in line 3.*

3. Then run `sh setup.sh` and it's done!

This method only works with GNOME.

PS: Make sure you have the */autostart* folder! If you don't, create it before step 3 with: `cd ~/.config && mkdir autostart`

### Use as a terminal command

If GNOME isn't your currently Desktop Manager, or if you don't want to listen to Bach everytime you login (shame on you), you can still run the script via command line.

To do it, open the file **Bach** and set the path to your local repository in the DIR variable.

After that, run: `sh setup_bin.sh`

Now you can get your daily dose of counterpoint with: `Bach`


Inspired by [Koan].

[Koan]: https://github.com/a-moreira/Koan
