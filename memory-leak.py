class CGcLeakA(object):
    def __init__(self):
        self._text = '#'*10

    def __del__(self):
        pass

class CGcLeakB(object):
    def __init__(self):
        self._text = '*'*10

    def __del__(self):
        pass

def make_circle_ref():
    _a = CGcLeakA()
    _b = CGcLeakB()
    _a._b = _b  # test_code_2
    _b._a = _a  # test_code_3
    print 'ref count0:a=%d b=%d' % \
        (sys.getrefcount(_a), sys.getrefcount(_b))
#   _b._a = None    # test_code_4
    del _a
    del _b
    try:
        print 'ref count1:a=%d' % sys.getrefcount(_a)
    except UnboundLocalError:
        print '_a is invalid!'
    try:
        print 'ref count2:b=%d' % sys.getrefcount(_b)
    except UnboundLocalError:
        print '_b is invalid!'