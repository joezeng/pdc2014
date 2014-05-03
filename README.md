PDC 2014
========

This is the judge program for the [Prisoner's Dilemma Challenge](http://codegolf.stackexchange.com/questions/26486/prisoners-dilemma-v-2-battle-royale) on the [Programming Puzzles and Code Golf Stack Exchange](http://codegolf.stackexchange.com/).

The preparation and scoring tools on this repository are licensed under the [MIT License](https://github.com/joezeng/pdc2014/blob/master/LICENSE). Entrant source files in "src/" are licensed under the [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/) unless otherwise specified.


Prereqs
-------

This program has only be tested on Ubuntu Linux, but should work on other POSIX systems with minimal tweaking. It will _not_ work on Windows as-is.

The program `timelimit` that limits execution time of programs must be installed.


How to Use
----------

The four Python files provided in the root directory are executed in this order:

    ./verify.py
    ./randgen.py >> pd_rand
	./compile.py
    ./test.py

### Procedure

Each entrant should be one source file, that will eventually be either compiled or interpreted by the host system. Place each entry into the directory `src` with a suitable filename. Make sure, however, that you do not name two files of different languages with the same name, as extensions are stripped. Also, make sure that you use the following extensions for specific languages:
	
* Python 2.x - `.py`
* Python 3.x - `.py3`

Run `verify.py` on the files and compare the hashes of the source file to the posted hash of each entrant. If there are no entrant hashes at all, then you can safely skip this step, as `verify.py` doesn't do anything else.

Run `randgen.py` to produce a `pd_rand` file with 500 random seeds for use as input. If you have more than 20 entrants, you'll need to run `randgen.py` more than once (once for every 20 entrants). In the official tournament, a pre-generated `pd_rand` file will be provided.

Run `compile.py` to compile each entry or insert a crunchbang line to tell the shell what interpreter to use.

Then, lastly, run `test.py` and watch the simulation go!

Good luck and have fun.
