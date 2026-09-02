# in Python there is a global scope and a local scope
# anything that is not inside a code block is in the global scope
# anything that is inside a code block has its own local scope

g = 'lunchtime'

def myFn():
    global g # now any reference to 'g' is the global one
    g = 'nearly'
    return g

def myOtherFn():
    g = 'local'
    return g

if __name__ == '__main__':
    print(g)
    print( myFn() )
    print(g)