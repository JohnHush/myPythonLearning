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

class Animal(object):
    def run(self):
        print "Animal is running"

class dog(Animal):
    def run( self ):
        print "Dog is runningiiiiiiiiiii"

class cat(Animal):
    def run( self ):
        print "cat is runningiiiiiiiiiii so fastttttttttt"

def run_twice(Animal):
    Animal.run()
    Animal.run()

def plus( x , y , f ):
    return f(x) + f(y)


if __name__ == "__main__":

    print plus( 10, -10 , abs )



