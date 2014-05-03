PDC 2014
========

This is the judge program for the [Prisoner's Dilemma Challenge](http://codegolf.stackexchange.com/questions/26486/prisoners-dilemma-v-2-battle-royale) on the [Programming Puzzles and Code Golf Stack Exchange](http://codegolf.stackexchange.com/).

The preparation and scoring tools on this repository are licensed under the [MIT License](https://github.com/joezeng/pdc2014/blob/master/LICENSE). Entrant source files in "src/" are licensed under the [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/) unless otherwise specified.


## Rules of the Game

In each round of this multiplayer, multi-round Prisoner's Dilemma, a player `A` can decide to "take 1" from some other player `B`. In this circumstance, `A`'s score increases by 1, while `B`'s score decreases by 2. This decision is allowed to happen between each ordered pair of players.

This is the only decision made for each player &ndash; either to "take 1" or not to "take 1" from each other player, which are homologous to defection and cooperation respectively. The effective payoff matrix between two players `P1` and `P2` looks as follows:

      P1/P2     P1 Take1   P1 Don't
    P2 Take1     -1/-1      -2/+1
    P2 Don't     +1/-2       0/ 0

## Tournament Procedure

The game will consist of `P * 25` rounds, where `P` is the number of participating players. All players start with a score of `0`. Each round will consist of the following procedure:

At the beginning of a round, each program will be given a history of the previous rounds **from standard input**, in the following format:

- One line containing 3 numbers, `P`, `D`, and `N`.

 - `P` is the total number of players in the game. Each player is randomly assigned an ID number from `1` to `P` at the beginning of the game.

 - `D` is the ID of the current player.

 - `N` is the number of rounds that have been played.
 
- `N` lines, each line representing the outcomes of a round. On line `k` of `N`, there will be some number `n_k` of ordered pairs `(a, b)`, separated by spaces, which represent that the player with ID `a` "took 1" from the player with ID `b` in that round.

- A uniformly random number `R` from `0` to `18446744073709551615` (2<sup>64</sup> - 1), to act as a pseudorandom seed. These numbers will be read from a pre-generated file, which will be released at the end of the tournament so that people can verify the results for themselves.

- One extra line that represents some form of state to be read into your program, if your program produced such an output in the previous round. At the beginning of the game, this line will always be empty. This line will not be modified by either the scoring code or other programs. 

Each program will then use its strategy to produce the following **to standard output**:

- A list of `K` numbers, which are the IDs of the programs it will "take 1" from this round. An empty output means it will do nothing.

- Optionally, one extra line representing some form of state to pass on to later rounds. This exact line will be fed back to the program in the next round.

Below is an example input for the beginning of the game for a player of ID `3` in a 4-player game:

    4 3 0
    4696634734863777023

Below is an example input for the same game with a few rounds already played:

    4 3 2
    (1, 2) (1, 3) (1, 4) (4, 2)
    (1, 3) (2, 1) (2, 4) (3, 1) (4, 1)
    4675881156406346380

Each program will be fed exactly the same input for a round except for the ID number `D` which is unique to each program.

Below is an example output in which player `3` takes 1 from everybody else:

    1 2 4

At the end of all the required rounds, the player with the highest final score will be the winner.

## Timeline

The coding for this tournament will last for a total of 7 days. The deadline for submissions is `2014-05-09 00:00 UTC`.

Do not post actual programs before this date &ndash; post the SHA256 hash of the source code of your program as a commitment. You may change this hash any time before the deadline, but commitments posted after the deadline will not be accepted for judgment. (Please use base 64 notation for your hashes, as my verification program spits out base 64 and it's a more compact notation.)

After the deadline is over, you will have 1 day (until `2014-05-10 00:00 UTC`) to post the actual source code of your program for your submission. If the SHA256 hash of your posted source code does not match any hash that you posted before the deadline, your code will not be accepted into the tournament.

After this, I will download all the submissions onto my own computer, and run all the tournament entries in this battle royale, hopefully posting the results within 2 days from then, by `2014-05-12 00:00 UTC`.

I will accept the answer with the highest score, and award a bounty of +100 to that answer if its final score is greater than `0`.

After the tournament is over, I will post the random seed file used to run the competition, and people may start posting other solutions trying to top the ones used in the tournament. However, they will not count for acceptance or the bounty.

## The Host Machine

I will be running these solutions on a virtual machine on my computer. This virtual machine will run Ubuntu Linux 14.04, with 2 gigabytes of RAM. My base machine has an Intel i7-2600K processor running at 3.40 GHz.

## Requirements

Your program must be written in a language for which a compiler or interpreter that will compile your program exists and is readily available for the latest version of Ubuntu Linux, so that I can run all the submissions and judge them in a virtual machine.

Your program must not take more than `2.000 seconds` to run each round. If your program runs out of time or produces an error, its output will be considered empty for that round.

Your program must be deterministic; that is, it must always return the same output for the same input. Pseudorandom solutions are allowed; however, their randomness must depend on the random seed given to it as input and nothing else. The seed file was generated using Python's `os.urandom`. It contains a total of 500 lines (more will be generated if necessary), and its SHA256 hash is `K+ics+sFq82lgiLanEnL/PABQKnn7rDAGmO48oiYxZk=`. It will be uploaded here once the tournament is over.
