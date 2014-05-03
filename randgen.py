#!/usr/bin/python
import os

for i in range(500):
	c = os.urandom(8)
	x = 0
	for a in c:
		x = x * 256 + ord(a)
	print x
