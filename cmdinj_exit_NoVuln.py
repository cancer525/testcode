#!/usr/bin/env python
import sys
import os

if __name__ == '__main__':
	filename = ""
	if len(sys.argv) < 2:
		print "Usage: ./%s filename" % sys.argv[0]
		filename = sys.argv[1]
		sys.exit(-1)

	test = 1
	cmd = test
	cmd = "cat " + filename
	cmd = "ls; cat" + filename
	print cmd

	os.system(cmd)

	sys.exit(0)

