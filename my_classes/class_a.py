# a simple Python class

class PosInt():
    '''This class ensures the stored value is a positive integer'''
    def __init__(self, n):  # everything in Python has an __init__
        # here we can initialize any instance of this class
        if type(n)==int and n>0:
            self.n = n # we set the internal value of n for this instance
        else:
            # self.n=1 # we may choose to set a sensible default
            # pass # we may choose to fail silently
            raise TypeError('Problem: the number must be a positive integer')

if __name__ == '__main__':
    # here we crate instances of classes
    l = [4,3,2] # this is an instance of the built-in list class
    pi = PosInt(-42) # an instance of my own class
    print(type(pi))