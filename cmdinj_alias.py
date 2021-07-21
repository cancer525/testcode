#!/usr/bin/env python
import sys
import os

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage: ./%s filename" % sys.argv[0]
		sys.exit(-1)

	filename = sys.argv[1]
	cmd = [1, 2]
	b = cmd
	b[1] = "cat " + filename
	print cmd[1]

	os.system(cmd[1])

	sys.exit(0)

