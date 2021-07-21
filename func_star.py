def fun1(*keys):
     print "keys type=%s" % type(keys)
     print "keys=%s" % str(keys)
     for i in range(0, len(keys)):
             print "keys[" + str(i) + "]=%s" % str(keys[i])

g_a = "123"

fun1(2,3,4,5)

def fun2(a ,b = 0 ,c = 2 ,d = g_a):
	print a, b, c, d

fun2(1,2,3,4)
fun2(b=1,c=2,a=3,d=4)
fun2(1,2,3)

def fun3(a, b=2, *c, **d):
	pass

def fun4(a, b=2, *c):
	print a, b, c

def fun5(a, b=2, **d):
	pass

def fun6(*c, **d):
	pass

def fun7(a=1, b=2, **d):
	print a, b, d
	pass

def fun8(a=1+2, b=fun2(1,2,3,4)):
	print a, b
	pass

fun4(a=1,b=3)
fun7(2+1, c=3)
fun8(a=1+2, b=1)

fun3(*a, **a)
