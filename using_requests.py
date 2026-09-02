# here we ask the user for an integer (via our utility module)
# Then grab data from the internet, id= user integer
from util import getNum

def getRemoteData():
    '''retrieve data from an API''' # API application programming interface
    # Ask user for an integer
    value = getNum()
    return value

if __name__ == '__main__':
    p = getRemoteData()
    print(p)