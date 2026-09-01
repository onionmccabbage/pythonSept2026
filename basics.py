# this is a comment in Python
# every Python file is a 'module'

# we can declare variables to be of a data type
 
a = 3       # integer
b = 7.6     # float
c = 'hello' # string (single quotes, double quotes or triple quotes)
d = '''this is a string using triple quotes
All formatting is preserved (return, tab etc)'''

# Boolean True and False
boo = True
print(boo)



print(a, b, c, d)
print( type(a), type(b), type(c) ) 

# we can carry out operations
e = a+b  # - and *
f = b/a
# some other operators
g = b**a # ** here means raise to the power
h = b//a # integer division (modulo)
j = b%a  # remainder division

print( e, f, g, h, j )

# mutability
# all variables are mutable
a = 8 # it no longer contains 3 it now contains 8
b = 'coffee' # it is no longer a float, it is now a string
# however some data types are immutable - string values are imutable
print(b, b[0], b[5]) # coffee c e

# other collections
# a list is created using []
l = [4, 6, 2, 'other'] # a list is an ordinal collection of any data types
print( l, type(l), l[3] )
# we may mutate members of a list
l[3] = 'changed'
print(l[3])
# we CANNOT mutate members of a string
# this line will fail
# b[0] = 'C'

b = 'but...'
print(b)

# we also have a collection called 'tuple'
# A tuple is an immutable ordinal collection of any data types
t = (5,4,3,a,b,c,'tatdaaaaa') # the () indicate a tuple
print(t)
print(type(t), t[4])

# accessing members of a collection
print(t[0:4]) # start at 0, stop before member 4
print(t[1:5])