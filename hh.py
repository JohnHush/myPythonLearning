class Student(object):

    def __init__( self , name , score ):
        self.name = name
        self.score = score

    def print_score( self ):
        print '%s: %s ' %(self.name, self.score)


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



