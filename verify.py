#!/usr/bin/python
import os, sys
import base64
import hashlib

source_files = os.listdir("src")

for filename in source_files:
	file = open("src/" + filename, "rb")
	sha256 = hashlib.sha256()
	sha256.update(file.read())
	print "%s:" % filename, base64.b64encode(sha256.digest())
