# Challenge Month 5

## Problem Statement
There's this game you really like, but just can't seem to solve. Perhaps this is the time to resort to....
less conventional methods ;) .

The game can be found [here](https://b1te.my/mayday/mayday.html). 

Note that you may need to zoom out a bit for it to work. Pressing Escape will bring you to the Menu as well. When
in the game, use WASD to mvoe and Q/E to fly (and left click to attack, you may need to move around to see
the boss). Note how the badly-designed boss regenerates their health once they reach a threshold. 
Taking a look under "Developer Options" may help, there seems to be way to directly
edit savedata there...

There is a concept called checksums. If you know about hashes, this is a similar idea- except checksums
were designed with security in mind, whereas checksums were more concerned about error checking, perhaps a networking
issue flipping a bit or something. 

Modifying the savefile directly in Developer options will probably result in a corrupt savefile, 
(Note there is no cursor indicator, just use the arrow keys to move up/down the characters at each index)
so by other methods such as Changing your name and seeing the known valid checksum it generates, 
you should reverse engineer the algorithm used to verify the checksum. 
Once you have done that, you can play around with the save data, looking for
anything that could help you defeat the boss in the game. Just play around with the data, and then "fix"
the checksum to get a valid savefile. Good luck!

Once you defeat the boss, he will give you a flag. Submit the flag [here](https://forms.gle/w7qcYDScmsFGF7rS8).
Again, good luck!
