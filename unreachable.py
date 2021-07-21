
import sys

def foo():
	print "reachable = True"
	return
	print "reachable = False"
	print "unreachable"

i = 0
if i>1:
	print "reachable = True"
	sys.exit()
	print "reachable = False"

print "reachable = True"
sys.exit()
print "reachable = False" 
print "done"	
