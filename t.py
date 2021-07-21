#!/usr/bin/env python
a=1
def p(i):
	print i
	j = 123
	def p1():
		print j
		def p2():
			print j
		p2()
	p1()
	k = j

def c():
	v = 0
	return 2

#c=1

p(12)
p('a')
p(3**3)
b = p
print c()**3
	#a.b.c.d(100)
#p(1)**2
#10(1,2)

#A.B.C[1](3)
#print c.type
#print 12.type

a=1
b=2
c,d,a,e.b.c.d=a,b,b,a
g[0]=1
print a, b, c, d, e, g

if 121 :
 pass

#if __name__ == '__main__':
	#i, o = do_connect("127.0.0.1", "2468")

#d = b, do_connect()
#a=1,2
#a,1=2
