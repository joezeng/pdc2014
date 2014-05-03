import sys
import re

line1 = [int(i) for i in sys.stdin.readline().split()]

players = line1[0]
pid = line1[1]
rounds = line1[2]

lines = []
victims = [0] * players
culprits = [0] * players
total_culprits = 0
scores = [0] * players

if rounds == 0:
	print
else:
	for i in range(rounds):
		takes = re.findall(r'\([0-9]+, [0-9]+\)', sys.stdin.readline())
		for take in takes:
			sides = [int(i) for i in re.findall(r'[0-9]+', take)]
			culprits[sides[0] - 1] += 1
			total_culprits += 1
	culprit_pairs = [(i+1, culprits[i]) for i in range(players)]
	culprit_pairs.sort(key=lambda x:(x[1], x[0]))
	culprit_pairs.reverse()
	j = 0
	while culprit_pairs[j][1] > total_culprits / players:
		if culprit_pairs[j][0] != pid:
			print culprit_pairs[j][0],
		j += 1
