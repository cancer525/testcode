#!/usr/bin/env python
import sys
import os

def catfile(filename):
	if 1>2:
		pass
	cmd = filename
	return cmd

	
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage: ./%s filename" % sys.argv[0]
		sys.exit(-1)

	file = "~/" + sys.argv[1]
	res = catfile(file)

	os.system(res)

	sys.exit(0)

