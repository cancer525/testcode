strHello = "the length of (%s) is %d" %('Hello World',len('Hello World'))
print strHello

print "nHex = %x,nDec = %d,nOct = %o" %(nHex,nHex,nHex)

print "PI = %f" % math.pi
print "PI = %10.3f" % math.pi
print "PI = %-10.3f" % math.pi
print "PI = %06d" % int(math.pi)

print "%.3s " % ("jcodeer")
print "%.*s" % (4,"jcodeer")
print "%10.3s" % ("jcodeer")

l = [1,2,3,4,'jcodeer']
print l

d = {1:'A',2:'B',3:'C',4:'D'}
print d
print d,"hello world",l
print d,"hello world",l,unused
print >> d
