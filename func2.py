
def f():
  print "hi"
  def f2():
	print "f2"
  f2()

def f2():
	print "-- f2"

f2()
f()
