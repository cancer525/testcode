def controlled_execution():  
    f = None  
    try:  
        f = open(filename, 'r')  
        thing = f.read()  
        #for thing in f:  
        yield thing  
    except IOError,e:  
        print 'Error %s' % str(e)  
    finally:  
        if f:   
            f.close()  
  
def test2():  
    for content in controlled_execution():  
        output(content)  

class controlled_execution(object):  
    def __init__(self):  
        self.f = None  
          
    def __enter__(self):  
        try:  
            f = open(filename, 'r')  
            content = f.read()  
            return content  
        except IOError ,e:  
            print 'Error %s' % str(e)  
            #return None  
  
    def __exit__(self, type, value, traceback):  
        if self.f:  
            print 'type:%s, value:%s, traceback:%s' % \
                    (str(type), str(value), str(traceback))  
            self.f.close()  
  
def test3():  
    with controlled_execution() as thing:  
        if thing:  
            output(thing) 

def test4():  
    with open(filename, 'r') as f:  
        output(f.read())  
  
    print f.read()  

