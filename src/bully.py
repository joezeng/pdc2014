import sys
import re

line1 = [int(i) for i in sys.stdin.readline().split()]

players = line1[0]
pid = line1[1]
rounds = line1[2]

lines = []
victims = [0] * players
total_victims = 0
culprits = [0] * players
scores = [0] * players

if rounds == 0:
	print
else:
	for i in range(rounds):
		takes = re.findall(r'\([0-9]+, [0-9]+\)', sys.stdin.readline())
		for take in takes:
			sides = [int(i) for i in re.findall(r'[0-9]+', take)]
			victims[sides[1] - 1] += 1
			total_victims += 1
	victim_pairs = [(i+1, victims[i]) for i in range(players)]
	victim_pairs.sort(key=lambda x:(x[1], x[0]))
	victim_pairs.reverse()
	j = 0
	while victim_pairs[j][1] > total_victims / players:
		if victim_pairs[j][0] != pid:
			print victim_pairs[j][0],
		j += 1
