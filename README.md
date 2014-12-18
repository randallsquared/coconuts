
I'm going to take some notes as I go.

The sample has a zero, while the second example doesn't (lowest is 248).

    $ grep '^0' flight_paths.txt
    $ grep '^.. ' flight_paths.txt
    $ grep '^... ' flight_paths.txt
    496 720 896
    787 1140 1765
    654 1029 1500
    422 841 1676
    248 761 2052
    458 697 956
    909 1450 1623
    901 967 330

I was about to check for duplicate starts, but it doesn't matter since they could have differing end points; no reason to try to simplify, that way.

My approach will be this.  


