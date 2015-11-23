def addVectors( v1 , v2 ):
    v3 = []
    i = 0
    while i<len( v1 ) and i<len(v2):
        v3.append( v1[i] + v2[i] )
        i = i +1
    if i == len( v1 ):
        v3.append( v2[i] )
        i = i+1
    if i == len( v2 ):
        v3.append( v1[i] )
        i = i+1
    return v3



if __name__ == '__main__':
    v1 = [1,2,3,4]
    v2 = [1,2,3]

    print addVectors( v1 , v2 )
