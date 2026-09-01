# indentation, logical 'if', loops
# input, print formatting
# functions - writing re-useable code

# here is a function which will take a value and convert it to an integer
def makeInt(x): # the colon : indicated the start of a code block (indentation)
    '''We often write a docstring to explain the purpose of a code block
    Here, we accept any value as x
    If it is a float we convert to an integer'''
    # a code block starts with indentation
    if type(x) == float:
        x = int(x) # convert the float to an int
    elif type(x) == str: # elif means else... if
        '''We can try to convert the string to an integer'''
        x = int(float(x))
    else: # handle any other outcome
        pass # do nothing
    return x # we send back the results of the function

# when we no longer indent our code, that is the end of the code block

# use our function (this code is not indented - it is 'immediate' code)
result = makeInt(5.7)
print(result, type(result)) # 5 class<int>
result2 = makeInt('42.5')
print(result2, type(result2))
