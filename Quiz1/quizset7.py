def f(L):
    result = []
    for e in L:
        if type(e) != list:
            result.append(e)
        else:
            return f(e)
    return result



if __name__ == '__main__':
    print f('3')
