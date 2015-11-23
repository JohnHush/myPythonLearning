
while True:
    try:
        x = int( raw_input( "Please enter a number: " ) )
        break
    except:
        print "Ooops, That was no valid number , try again!!"
        raise
