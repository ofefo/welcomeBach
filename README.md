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

The project has grown and currently supports a few other composers, and it's possible to import more.

Lists of your past listens are saved inside the **listens** folder.

### Installation (with Gnome as a DE)

To install the script, run `./install.sh gnome` and you're done!

This method only works with GNOME, and will always return a piece by Bach!

### Use as a terminal command

If GNOME isn't your current Desktop Environment, or if you don't want to listen to Bach at every startup (shame on you), you can still run the script via command line.

To do it, run: `./install.sh`

Now you can get your daily dose of counterpoint with: `welcomebach`

By default, it returns 3 links, but you can pass a value as an argument to get more results (e.g. `welcomebach -v=5`).<br/>
If you want to relisten to the last piece, run it with the *--relisten* flag: `welcomebach -r`<br/>
To listen to another composer, try it with the *--composer* flag: `welcomebach -c=Debussy`<br/>
All flags should work normally with any composer.

### Adding more composers

If you want to include more catalogues of compositions, you can try the *catalogueDL* script. It was made to work with tables and lists found on wikipedia. The resulting catalogue might need some quick fixes.

### Additional info

This is a work in progress.

It was inspired by [Koan].

welcomeBach is licensed under GNU GPLv2 or later, feel free to make it better.

[Koan]: https://github.com/a-moreira/Koan
[oeuvre of J.S. Bach]: https://en.wikipedia.org/wiki/Bach-Werke-Verzeichnis
