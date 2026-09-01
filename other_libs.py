# we may use any of the built in Python libraries
# we may choose to import a library 'as' to make references easier
import datetime as dt # datetime is part of the Python Standard Library

# we may also choose to only import a part of a library
from datetime import datetime

def showToday():
    '''return a nicely formated date'''
    # now = datetime.datetime.date( datetime.datetime.today() )
    # now = dt.datetime.date( dt.datetime.today() )
    now = datetime.date( datetime.today() )
    prettyDate = datetime.strftime(now, "%Y %d-%m")
    return prettyDate


# immediate code
print( showToday() )