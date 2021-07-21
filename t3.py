#!/usr/bin/env python  
  
from __future__ import with_statement   
  
filename = 'for_test.txt'  
  
def output(content):  
    print content  
  
#functio solution  
def controlled_execution(func):  
    #prepare thing  
    f = None  
    try:  
        #set thing up  
        f = open(filename, 'r')  
        content = f.read()  
        if not callable(func):  
            return  
        #deal with thing   
        func(content)  
  
    except IOError, e:  
        print 'Error %s' % str(e)  
  
    finally:  
        if f:   
            #tear thing down  
            f.close()  
  
def test():  
    controlled_execution(output)  
  
test()  
