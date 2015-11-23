import copy

def findAll(wordList, lStr):
    """assumes: wordList is a list of words in lowercase.
    lStr is a str of lowercase letters.
    No letter occurs in lStr more than once
    returns: a list of all the words in wordList that contain
    each of the letters in lStr exactly once and no
    letters not in lStr."""
    D = {}
    lst = []
    for c in lStr:
        if c in D.keys():
            D[c] += 1
        else:
            D[c] = 1

    for word in wordList:
        flag = True
        D_copy = copy.deepcopy(D)
        for c in word:
            if c not in D_copy.keys():
                flag = False
                break
            else:
                D_copy[c] -= 1
                if D_copy[c] < 0:
                    flag = False
                    break
        if flag == True:
            lst.append( word )
    return lst

def findAll2( wordList , letters ):
    result = []
    letters = sorted( letters )
    for w in wordList:
        w = sorted(w )
        if w == letters:
            result.append(w )
    return result

if __name__ == '__main__':
    wordList = ['string','dude','bitch','hello','yoh','goodbye','sandy']
    lStr = 'doubleclickdhy'

    print findAll( wordList , lStr )
