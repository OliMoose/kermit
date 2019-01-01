# kermit
*The code for the Kermit discord bot! Have fun*

Kermit runs on the rewrite branch of discord.py, so if there are errors check you have the right version

this whole thing runs on a lightweight modular system, with the initial program modular.py loading all the commands from ./coms/ !

all the commands in ./coms/ are Objects, that have a parent Command object (found in \_command.py)

so each individual command doesn't have as much programming, since the Command object handles most of the wrapping and util commands for each one

some of the commands need to save and edit images/pickled lists- that's what ./assets/ is for

and excuse the messy code in places aha,
deepfry and ytmp3 in particular are awful to read


ALSO run.sh is just a shell script that keeps on running kermit, so if the program crashes/kills itself/kermits suicide it immediately restarts
