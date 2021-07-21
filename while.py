#!/usr/bin/env python

a = 2;
b = 1;
c = 1;

while a>1:
	b = 2
	a -= 1
	if b > 1:
		continue
	if a < 0:
		break;

print a, b, c	

a = 2;
b = 1;
c = 1;

while 1:
#if 1:
	while a>1:
		b = 2
		a -= 1
	else:
		c = 2
		d = 1
		break;

print a, b, c, d	
del a,b
del d
