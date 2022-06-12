# welcomeBach

Receive a list of YouTube links for recordings of a different piece by Bach at each startup.

```
Today's Bach is: 
  BWV 1050 – Brandenburg Concerto No. 5 in D major

Bach: Brandenburg Concerto No. 5 in D major, BWV 1050 (Freiburger Barockorchester)
https://www.youtube.com/watch?v=_V7oujd9djk

Bach - Brandenburg Concerto No. 5 in D major BWV 1050 - Sato | Netherlands Bach Society
https://www.youtube.com/watch?v=LHjbRMIIhuM

Johann Sebastian Bach  Brandenburg Concerto no 5 D major BWV 1050
https://www.youtube.com/watch?v=sA15dEnJEtQ
```

This script was made to provide a consistent way to listen to the complete [oeuvre of J.S. Bach], as it spans more than a thousand pieces, considered an essential part of the western musical repertoire.

The project has grown and currently supports a few other composers, being possible to import more from Wikipedia or IMLSP pages.

Lists of your past listens are saved inside the **listens** folder.

## Installation (with Gnome as a DE)

To install the script, run `./install.sh gnome` and you're done!

(PS: this only works with GNOME, and will always return a piece by Bach!)

## Use as a terminal command

If you're not using GNOME, or if you don't want to listen to Bach at every startup (shame on you), you can run it in command line.

To do it, run: `./install.sh`

Now you can get your daily dose of counterpoint with: `welcomebach`

* Try another **composer**: `welcomebach -c Debussy`, `welcomebach -c Saariaho`, etc.<br/>
* **Download** another catalogue: `welcomebach -d` (should work with pages from wikipedia or IMLSP, but will probably need some quick fixes)
* Open links with **mpv**: `welcomebach -m`
* **Relisten** to a piece: `welcomebach -r`, `welcomebach -r -c Debussy`<br/>
* Change the **verbosity**: `welcomebach -v 5`<br/>

You can get help with `welcomebach -h`

## Additional info

This is a work in progress.

It was inspired by [Koan].

welcomeBach is licensed under GNU GPLv2, feel free to make it better.

[Koan]: https://github.com/a-moreira/Koan
[oeuvre of J.S. Bach]: https://en.wikipedia.org/wiki/Bach-Werke-Verzeichnis
