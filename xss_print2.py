req = self.request()  # fetch the request object

eid = req.field('eid',None) # tainted request message

print 'Employee ID: %s' % eid
