# range, generators and comprehension are dead handy features

# using range
r = range(0, 10**10, 10) # start, stop-before, step (step is optional defaults to 1)


# using comprehension (means dont leave anything out)
# c will be a comprehensive generator of all the squares of the range
# NB the values do not exist in memory, they are generated on demand
c = (i**2 for i in range(0,10)) # this comprehensively deals with each member of the range to do a calculation

# using generator to create in-memory values
l = [i**3 for i in range(-10,11)] # [] always makes a list

if __name__ == '__main__':
    # here we exercise the code in this module
    print(r, type(r))
    # for _ in r:
    #     # print(_) # it is fairly common to use underscore _ as an iterator
    #     pass
    print(c, type(c))
    for _ in c:
        # anything raised to 0.5 is the square root
        print(f'{_**0.5} squared is {_}')
    print(l, type(l))