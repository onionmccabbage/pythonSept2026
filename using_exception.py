# We often need to handle exceptions

# we may choose to provide function arguments or not (within the brackets)
def askUser():
    '''ask for a number from the user
    NB we will handle exceptions if it is not a number'''
    d = input('please enter a number: ')
    # convert to a numerical value
    try:
        n = int(float(d))
        return n
    except Exception as err:
        print(f'problem: {err}')

# immediate code
target = 50
u =-99
while u != target:
    u = askUser()
