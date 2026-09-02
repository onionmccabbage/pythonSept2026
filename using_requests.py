# here we ask the user for an integer (via our utility module)
# Then grab data from the internet, id= user integer
from util import getNum
import requests

def getRemoteData():
    '''retrieve data from an API''' # API application programming interface
    # Ask user for an integer
    value = getNum()
    # return value
    api = 'http://jsonplaceholder.typicode.com/photos' # ANY public API can be accessed
    # This is the sort of thing that could go wrong
    try:
        # we will use 'get' to retrieve all the JSON text
        # this is asynchronous - it takes time
        # so the requests library knows to wait (or timeout)
        response = requests.get(f'{api}/{value}') # this will make a request to the URL
        # we know the data is JSON in this case
        # this next line automatically converts the data into a Python structure 
        photos = response.json() # or xml, text, html etc.
        # NB Python automatically converts the JSON text into a Python structure
        return photos # we have a list of dict
    except Exception as err: # we should consider using specific exception types
        print(f'Connection error: {err}')

if __name__ == '__main__':
    p = getRemoteData()
    print(p)
    print(type(p))
    print(p['title']) # grab just the title from the returned dictionary