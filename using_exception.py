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
    except ValueError as ve: # we can handle specific kinds of exception
        print(f'{d} is not a number')
    except Exception as err: # this catches all types of exception (unless already handled)
        print(f'problem: {err}')
    finally:
        ''' this is a good place to tidy up any left-over values'''
        print('the finally block always runs')

# immediate code
target = 50
u =-99
while u != target:
    u = askUser()
