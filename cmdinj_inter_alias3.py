#!/usr/bin/env python
import sys
import os

def catfile(filename):
	cmd = "cat " + filename
	print cmd
	os.system(cmd)

	cmd_t = filename
	a[0] = cmd_t;
	cmd_t = a[0]
	os.system(cmd_t[0])
	
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage: ./%s filename" % sys.argv[0]
		sys.exit(-1)

	file = ""
	if 1>2:
		file = "~/" + sys.argv[1]

	a[0] = file;		
	catfile(a)

	sys.exit(0)

