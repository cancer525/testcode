#!/usr/bin/env python
import sys
import os

def foo(cmd):
	file = "~/" + sys.argv[1]
	a = "cat " + file
	cmd[0] = a;
	
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage: ./%s filename" % sys.argv[0]
		sys.exit(-1)

	foo(cmd)

	print cmd[0]
	os.system(cmd[0])
