import sys
import re
import random

line1 = [int(i) for i in sys.stdin.readline().split()]

players = line1[0]
pid = line1[1]
rounds = line1[2]

for i in range(rounds):
	sys.stdin.readline()
rseed = int(sys.stdin.readline().strip())
random.seed(rseed)
for i in range(players):
	if i+1 != pid and random.random() < 0.5:
		print i+1,
print
