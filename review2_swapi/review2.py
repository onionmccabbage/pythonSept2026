import requests
from util.sanitize import cleanup

def get_data(category, id):
    # full_path = f'https://jsonplaceholder.typicode.com/{category}/{id}'
    full_path = f'https://swapi.dev/api/{category}/{id}'
    # this would be a really good place to use try-except
    res = requests.get(full_path)
    j = res.json() # we just want the json data
    return j # return the data as a dict

def main():
    # ask the user for a category and an id
    which_cat = input('which category? ')
    which_id  = input('which id (1-10)? ')
    # use our sanitize module to clean up some data
    cleaned = cleanup(category=which_cat, id=which_id)
    # make a request and return the json
    data = get_data(category=cleaned['category'], id=cleaned['id'])
    # NB be careful - here we have double quotes inside single quotes (which is fine)
    resultString = f'Category {cleaned["category"]} member {cleaned["id"]} gives the following:\n'
    for k, v in data.items(): # here we iterate over a dictionary key:value pairs
        print(f'\t{k}: {v}')
        resultString += f'\t{k}: {v}\n'
    print(resultString)

if __name__ == '__main__':
    main()