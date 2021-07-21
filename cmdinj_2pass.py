#!/usr/bin/env python
import sys
import os

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage: ./%s filename" % sys.argv[0]
		sys.exit(-1)

	filename = sys.argv[1]
	cmd = "cat " + filename
	cmd = "ls; cat" + filename
	tmp = cmd
	cmd = tmp
	print cmd

	os.system(cmd)

	sys.exit(0)

