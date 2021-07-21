#!/usr/bin/env python
import sys
import os

def foo(cmd, cmd2):
	a = cmd[0]
	cmd2[0] = a;
	
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage: ./%s filename" % sys.argv[0]
		sys.exit(-1)

	file = "~/" + sys.argv[1]
	cmd = "cat " + file
	foo(cmd, cmd2)

	print cmd2[0]
	os.system(cmd2[0])
