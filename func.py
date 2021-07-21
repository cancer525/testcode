result = f2(1,2)

def f2(x,n):
   t1 = clock()
   r = x/pow(2,n)
   t2 = clock()
   print (t2-t1)
   print r
   t2 = clock()
   r = x>>n
   t3 = clock()
   print (t3-t2)
   print r
   def t():
	print "hello"
   t()

def t():
   print "hello world"

result = f2(1,2)
