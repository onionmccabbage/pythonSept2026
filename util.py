# a utility module

def myGen(start=0, stop_before=5): # any function may take defaults for its arguments
    '''return a generator for values from start to stop_before '''
    g = (i for i in range(start, stop_before))
    return g

def getNum():
    'Ask the user for a number. Non-numeric entries raise an exception'
    try:
        # remember every input is ALWAYS a string
        n = input('Please enter an integer: ')
        num = int(float(n))
        return num
    except Exception as err:
        print(f'The value is not a number {err}')
        return 1 # a default number returned if the user did not enter a numeric value

if __name__ == '__main__':
    # code here will only execute if this module is run directly
    # IE the following code will NOT run if this module is imported elsewehere
    my_num = getNum()
    print(my_num)