#!/usr/bin/env python
import sys
import os

def foo(filename):
	cmd = "cat " + filename
	print cmd
	
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage: ./%s filename" % sys.argv[0]
		sys.exit(-1)

	file1 = ""
	file2 = ""
	if 1>2:
		file1 = "~/"

	foo(file1)

