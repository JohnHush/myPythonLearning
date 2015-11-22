import functools

class Student(object):

    def __init__( self , name , score ):
        self.name = name
        self.score = score

    def print_score( self ):
        print '%s: %s ' %(self.name, self.score)

    def get_score( self ):
        return self.score
def build( x , y ):
    return lambda : y*y + x*x

def log(text):
    if callable(text):
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print 'begin call: ' + text.__name__
            text(*args, **kw)
            print 'end call: ' + text.__name__
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print 'begin call: ' + text
                func(*args, **kw)
                print 'end call: ' + text
            return wrapper
        return decorator

@log
def  now1():
    print 'doing1...'

@log('text')
def now2():
    print 'doing2...'

if __name__ == "__main__":

    now1()
    now2()


