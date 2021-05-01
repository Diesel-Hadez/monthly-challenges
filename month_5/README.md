# Challenge Month 4

## Problem Statement
There's this game you really like, but just can't seem to solve. Perhaps this is the time to resort to....
less conventional methods.

The game can be found [here](https://b1te.my/mayday/mayday.html). 

Note that you may need to zoom out a bit for it to work. Pressing Escape will bring you tot he Menu as well. When
in the game, use WASD to mvoe and Q/E to fly (and left click to attack.). Note how the badly-designed boss
regenerates their health. Taking a look under "Developer Options" may help, there seems to be way to directly
edit savedata there...

There is a concept called checksums. If you know about hashes, this is a similar idea- except checksums
were designed with security in mind, whereas checksums were more concerned about error checking. Modifying
the savefile directly in Developer options will probably result in a corrupt savefile, so by other methods
such as Changing your name and seeing known valid checksum, you should reverse engineer the algorithm
used to verify the checksum. Once you have done that, you can play around with the save data, looking for
anything that could help you defeat the boss in the game. Just play around with the data, and then "fix"
the checksum. Good luck!
