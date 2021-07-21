#!/usr/bin/env python
import sys
import os

def catfile(filename = sys.argv[1]):
	cmd = "cat " + filename
	print cmd

	os.system(cmd)
	
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage: ./%s filename" % sys.argv[0]
		sys.exit(-1)

	file = ""
	if 1>2:
		file = "~/" + sys.argv[1]
	#catfile(file)
	catfile(filename = file)
	#a = sys.argv[0]
	#catfile(a)
	#catfile()

	sys.exit(0)

