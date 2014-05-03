import sys
import re

line1 = [int(i) for i in sys.stdin.readline().split()]

players = line1[0]
pid = line1[1]
rounds = line1[2]

lines = []
scores = [0] * players

if rounds == 0:
	for i in range(players):
		if i+1 != pid:
			print i+1,
	print
else:
	for i in range(rounds):
		takes = re.findall(r'\([0-9]+, [0-9]+\)', sys.stdin.readline())
		for take in takes:
			sides = [int(i) for i in re.findall(r'[0-9]+', take)]
			scores[sides[0] - 1] += 1
			scores[sides[1] - 1] -= 2
	score_pairs = [(i+1, scores[i]) for i in range(players)]
	score_pairs.sort(key=lambda x:(x[1], x[0]))
	score_pairs.reverse()
	taken = 0
	j = 0
	while taken < (players) / 2:
		if score_pairs[j][0] != pid:
			print score_pairs[j][0],
			taken += 1
		j += 1
