#!/usr/bin/env python
import sys
import os

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage: ./%s filename" % sys.argv[0]
		sys.exit(-1)

	filename = sys.argv[1]
	cmd = 2
	cmd = "ls; cat" + filename
	print cmd

	os.system(cmd)
	cmd = 2 # test for dyn-symbol-type

	sys.exit(0)

