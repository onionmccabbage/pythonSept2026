# a simple Python class

# a class encapsulates properties and methods we may need
# properties are one or more values we wish to store
# methods are operations we may choose to carry out with our class

# e.g. the list class: 
# properties: it can store an ordinal collection of values
# methods: we can append, remove, insert values to the list

# a custom class
class PosInt():
    '''This class ensures the stored value is a positive integer'''
    def __init__(self, n):  # everything in Python has an __init__
        # here we can initialize any instance of this class
        self.n = n # this calls our setter function
    # what we do to ensure propeties are AWLAYS validated...
    @property # this is called a decorator (see the @ sign) 
    def n(self): # this is the getter-function
        return self._n # note the underscore
    @n.setter # another decorator
    def n(self, new_n):# this is the setter-function
        if type(new_n)==int and new_n>0:
            self._n = new_n # we set the internal value of n for this instance
        else:
            # self.n=1 # we may choose to set a sensible default
            # pass # we may choose to fail silently
            raise TypeError('Problem: the number must be a positive integer')


if __name__ == '__main__':
    # here we crate instances of classes
    l = [4,3,2] # this is an instance of the built-in list class
    pi = PosInt(42) # an instance of my own class
    print(type(pi))
    # how do we access the class properties (n in this case)
    print( pi.n )
    # we're not quite done yet....
    pi.n = 'changed'
    print( pi.n )
