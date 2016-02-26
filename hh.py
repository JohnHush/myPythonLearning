def test( x ,  memo = None ):
    if memo == None:
        memo = []
    else:
        memo.append( x )

    for i in range( 10 ):
        test( i , memo )
    return memo


test( 1 )
