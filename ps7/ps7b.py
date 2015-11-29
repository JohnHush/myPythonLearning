import math
import random
import pylab

class SolutionCoinFlip( object ):
    
    def __init__( self , nflip , ntrial ):
        self.nflip  = nflip
        self.ntrial = ntrial

    def getSequences( self ):
        '''
        this function flips the coin 3 times for a trial,
        and the experiment did for ntrial times,
        the return value is a returned solution in a list form
        '''
        sequence = []
        sub_sequence = []
        for _ in xrange( self.ntrial ):
            sub_sequence = []
            for _ in xrange( self.nflip ):
                if random.random() < 0.5:
                    sub_sequence.append( 'H' )
                else:
                    sub_sequence.append( 'T' )
            sequence.append( sub_sequence )
        return sequence

    def exactMatchNum( self , lst ):
        '''
        return the exactly match time with the Sequence
        input a list with number nflip,wrong number will
        raise error
        '''
        if len( lst ) != self.nflip:
            raise ValueError( 'input list in function exactMatchNum gets a wrong length!' )
        count =0

        for item in self.getSequences():
            if lst == item:
                count += 1
        return count

def coinFlip():
    num_test = 1000000
    case1 = ['H','T','H']
    solution = SolutionCoinFlip( 3 , num_test )
    return float(solution.exactMatchNum( case1 ))/num_test

print coinFlip()
