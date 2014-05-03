#!/usr/bin/python

# Program-compiling script for PDC 2014

import os
import shutil

# remove previous temp files
try:
	shutil.rmtree("exe")
except:
	print "Directory 'exe' already doesn't exist."

try:
	os.remove("gamestate")
except:
	print "File 'gamestate' already doesn't exist."

try:
	os.remove("output")
except:
	print "File 'output' already doesn't exist."

files = os.listdir("src")
os.mkdir("exe")

for filename in files:
	# files in python
	if filename[-3:] == ".py":
		fin = open("src/" + filename, "r")
		fout = open("exe/" + filename[:-3], "w")
		fout.write("#!/usr/bin/python\n")
		for line in fin:
			fout.write(line)
		fin.close()
		fout.close()
		os.chmod("exe/" + filename[:-3], 0755)
	# files in python 3
	if filename[-4:] == ".py3":
		fin = open("src/" + filename, "r")
		fout = open("exe/" + filename[:-4], "w")
		fout.write("#!/usr/bin/python3\n")
		for line in fin:
			fout.write(line)
		fin.close()
		fout.close()
		os.chmod("exe/" + filename[:-3], 0755)
