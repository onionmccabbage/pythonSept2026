# range, generators and comprehension are dead handy features

# using range
r = range(0, 10**10000000, 10) # start, stop-before, step (step is optional defaults to 1)


# using comprehension



# using generator


if __name__ == '__main__':
    # here we exercise the code in this module
    print(r, type(r))
    # for _ in r:
    #     # print(_) # it is fairly common to use underscore _ as an iterator
    #     pass