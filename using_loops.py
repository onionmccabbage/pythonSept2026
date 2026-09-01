# There are several kinds of loop in Python
# for loop
# while loop
# we will also meet 'range'

for i in range(0, 10, 2): # start, stop-before, step (can be negative)
    print(i)

x = 0
# a little guessing game
while x != 5: # != means 'not equal to'
    x = int(float(input('guess the number: ')))

# the dictionary collection
# a dict is a non-ordinal mutable collection of any data type as key:value pairs
d = {'fn':'Floella', 'ln':'Benjamin', 'attrib':'Dame'} # here the {} indicate a dictionary
d['attrib'] = 'Rt Hon'
print(d, type(d))
print(d['fn'])