import random

def simThrows( numFlips ):
    num = 0
    sim = ['']*10
    print sim
    for i in xrange( numFlips ):
        for j in xrange( 10 ):
            if random.random() < 0.5:
                sim[j] = 'H'
            else:
                sim[j] = 'T'
        for j in xrange( 7 ):
            if sim[ j:j+4 ] == ['H','H','H','H']:
                num += 1
    return float(num)/numFlips

print simThrows( 10000 )
