# Lambda functions

# Conditional (named lambda)
check = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(check(5))   
print(check(-3))  
print(check(0))

def myfunc(n):
  return lambda a : a * n

doubler = myfunc(2)
tripler = myfunc(3)

print(doubler(11))
print(tripler(11))

# with filter
even = filter(lambda x: x % 2 == 0, range(0,11))
print(list(even))