#!/usr/bin/env python
import sys

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage: ./%s filename" % sys.argv[0]
		sys.exit(-1)

	filename = sys.argv[1]
	exec "ls"
	cmd = "ls; cat" + filename
	exec cmd
