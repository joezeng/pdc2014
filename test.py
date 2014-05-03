#!/usr/bin/python

from subprocess import call
import textwrap
import random
import os

# config parameters

contestant_dir = "exe"
log_player_outputs = False
show_game_log = True
pause_between_rounds = False
random_order = True
totally_random_order = True

# run code

filenames = os.listdir(contestant_dir)
filenames.sort()

if random_order:
	if not totally_random_order:
		random.seed(4164398143650650814)
	random.shuffle(filenames)

n_players = len(filenames)

states = [""] * n_players
scores = [0] * n_players

n_rounds = n_players * 25

rounds_played = 0
game_log = ""

randseeds = [int(i) for i in open("pd_rand").readlines()]

def play_round(player):
	global filenames, n_players, states, rounds_played, game_log
	
	if log_player_outputs:
		print "Player %d:" % (player + 1),
	text_input = "%d %d %d\n%s%d\n%s" % (n_players, player + 1, rounds_played, game_log, randseeds[rounds_played], states[player])

	fout = open("gamestate", "w")
	fout.write(text_input)
	fout.close()

	p = call(["timelimit -t 2 %s/%s" % (contestant_dir, filenames[player])], stdin=open("gamestate", 'r'), stdout=open("output", 'w'), shell=True)

	fin = open("output", "rb")
	take_output = fin.readline()
	if log_player_outputs:
		print take_output.strip()
	takes = take_output.split()
	state = fin.readline()
	fin.close()
	return (takes, state)

for n_round in xrange(n_rounds):
	print textwrap.dedent("""\
	=================
	= Round %s =
	=================""") % repr(rounds_played + 1).ljust(7)
	log_entry = ""
	for x in range(n_players):
		output = play_round(x)
		for victim in output[0]:
			log_entry += "(%s, %s) " % (x + 1, victim)
			scores[int(victim) - 1] -= 2
			scores[x] += 1
		states[x] = output[1]
	game_log += log_entry + "\n"
	rounds_played += 1
	print "\nScores:",
	for n in xrange(len(scores)):
		print scores[n],
	print
	print
	if pause_between_rounds:
		raw_input("Press Enter to continue...")

if show_game_log:
	print "Game log: \n" + game_log
print "Final scores:"
for n in xrange(len(scores)):
	print filenames[n], scores[n]
