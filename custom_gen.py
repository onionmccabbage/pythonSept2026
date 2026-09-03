from datetime import datetime

# Python had built-in generator syntax
g = (i**2 for i in range(0,50))

# we may choose to create our own custom generator
def makeDT():
    '''This custom generator will yield a date-time stamp whenever required'''
    while True: # this is an endless loop
        now = datetime.now()
        dt_str = now.strftime('%d-%m-%y %H:%M:%S')
        # to make an ordinary function behave as a generator, we use 'yield' isntead of 'return'
        yield dt_str

# any generator will be destroyed when the module stops running

if __name__ == '__main__':
    df = makeDT() # here is an instance of our custom generator
    print(type(df))
    t1 = df.__next__() # grab the next value from our generator
    print(t1)
    t2 = df.__next__() # grab the next value from our generator
    print(t2)
    t3 = df.__next__() # grab the next value from our generator
    print(t3)
    t4 = df.__next__() # grab the next value from our generator
    print(t4)
    t5 = df.__next__() # grab the next value from our generator
    print(t5)
    t6 = df.__next__() # grab the next value from our generator
    print(t6)

