#!/usr/bin/env python
import sys
import os

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage: ./%s filename" % sys.argv[0]
		sys.exit(-1)

	while 1>2:
		filename = sys.argv[1]
		cmd = "cat " + filename
		print cmd

	os.system(cmd)

	sys.exit(0)

