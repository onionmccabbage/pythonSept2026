# a module to get data from an API URL using a generator
import requests

from util import myGen

def getPhotos():
    '''use a generator to get individual data'''
    api = 'https://jsonplaceholder.typicode.com'
    category = 'photos'
    g = myGen(1, 6) # override or let the defaults operate
    # we need somewhere to store all the retured data collectively
    photos = [] # we start with an empty list
    # loop over the generator vaules
    for i in g:
        try:
            # use requests to get a photo
            response = requests.get(f'{api}/{category}/{i}')
            # add the returned data to a list
            photos.append(response.json())
        except Exception as err:
            print(f'Ooops {err}')
    # return all the returned photos in a list
    return photos

if __name__ == '__main__':
    p = getPhotos()
    print(p)
