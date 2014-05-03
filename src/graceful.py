import sys
import re

line1 = [int(i) for i in sys.stdin.readline().split()]

players = line1[0]
pid = line1[1]
rounds = line1[2]

lines = []

if rounds == 0:
	pass
else:
	for i in range(rounds):
		lines.append(sys.stdin.readline())
	lastline = lines[-1]
	takes = re.findall(r'\([0-9]+, [0-9]+\)', lastline)
	for take in takes:
		sides = [int(i) for i in re.findall(r'[0-9]+', take)]
		if sides[1] == pid:
			print sides[0],
	print
