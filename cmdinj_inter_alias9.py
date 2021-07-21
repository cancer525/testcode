#!/usr/bin/env python
import sys
import os

def catfile(filename):
	os.system(filename[0])
	
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage: ./%s filename" % sys.argv[0]
		sys.exit(-1)

	file = "~/" + sys.argv[1]
	catfile(file)

	sys.exit(0)

