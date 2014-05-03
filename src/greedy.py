import sys

line1 = sys.stdin.readline()
n = [int(i) for i in line1.split()]
for i in range(n[0]):
	if i+1 != n[1]:
		print i+1,
print
