# welcomeBach

Receive a list of YouTube links for recordings of a different piece by Bach at each startup.

```
Today's Bach is: 
  BWV 1079 – Musikalisches Opfer (The Musical Offering)

https://www.youtube.com/watch?v=rN2p3NgqWos
https://www.youtube.com/watch?v=23yNGer9Wqs
https://www.youtube.com/watch?v=AzT_elDRLJM
```

This script was made to provide a consistent way to listen to the complete [oeuvre of J.S. Bach], as it spans more than a thousand pieces, considered an essential part of the western repertoire.

The project has grown and currently supports a few other composers, and you can import more with the script *catalogueDL*, which was developed to work with tables found on wikipedia.

Lists of your past listens are saved inside the **listens** folder.

### Installation (with Gnome as a DE)

To install the script, run `./install.sh gnome` and you're done!

This method only works with GNOME, and will always return a piece by Bach!

### Use as a terminal command

If GNOME isn't your current Desktop Environment, or if you don't want to listen to Bach at every startup (shame on you), you can still run the script via command line.

To do it, run: `./install.sh`

Now you can get your daily dose of counterpoint with: `welcomebach`

By default, it returns 3 links, but you can pass a value as an argument to get more results (e.g. `wlcomebach -v=5`).

If you want to relisten to the last BWV, run it with the *--relisten* flag: `welcomebach -r`

To listen to another composer, try it with the *--composer* flag: `welcomebach -c=Debussy`

Inspired by [Koan].

### License

welcomeBach is licensed under GNU GPLv2 or later.

[Koan]: https://github.com/a-moreira/Koan
[oeuvre of J.S. Bach]: https://en.wikipedia.org/wiki/Bach-Werke-Verzeichnis
