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

## Installation (with Gnome as a DE)

To install the script, run `./install.sh gnome` and you're done!

(PS: this only works with GNOME, and will always return a piece by Bach!)

## Use as a terminal command

If you're not using GNOME, or if you don't want to listen to Bach at every startup (shame on you), you can run it in command line.

To do it, run: `./install.sh`

Now you can get your daily dose of counterpoint with: `welcomebach`

* By default you get 3 links, but you can change the verbosity: `welcomebach -v=5`<br/>
* Relisten to the last piece with: `welcomebach -r`<br/>
* Try another composer: `welcomebach -c=Debussy`, `welcomebach -c=Saariaho`, etc.<br/>
* If you have **mpv** installed, you can open the links with it using: `welcomebach -m`
* To add another composer, run: `welcomebach -d` (should work with pages from wikipedia or IMLSP, but will probably need some quick fixes)

You can get help with `welcomebach -h`

## Additional info

This is a work in progress.

It was inspired by [Koan].

welcomeBach is licensed under GNU GPLv2 or later, feel free to make it better.

[Koan]: https://github.com/a-moreira/Koan
[oeuvre of J.S. Bach]: https://en.wikipedia.org/wiki/Bach-Werke-Verzeichnis
