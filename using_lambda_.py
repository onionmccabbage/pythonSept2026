# Lambda functions
# idea is you need a quick little function without all the multiple lines
# we may choose to give our lambda function a name
# or it may be anonymous

# use case: act conditional upon something
chk = lambda x: "Positive" if x>0 else "Negative" if x<0 else "Zero"
print(chk(3))
print(chk(-3))
print(chk(0))

# use case: anonymous function
even = filter(lambda x: x%2==0, range(0,11))
print(list(even))

# use case: combine with normal function
def fn(n):
    return lambda a:a*n

dbl = fn(2)
trp = fn(3)

print( dbl(11) )
print( trp(11) )