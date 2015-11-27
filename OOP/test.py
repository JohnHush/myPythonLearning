class person( object ):
    num = 0 

    def __init__( self , name ):
        self.name = name
        self.num  = person.num
        person.num += 1
    
    def print_person( self ):
        print self.name + ',' + str( self.num )

if __name__ == '__main__':
    Lisa = person( 'Lisa' )
    John = person( 'John' )

    Lisa.print_person()
    John.print_person()

    print person.num==Lisa.num
