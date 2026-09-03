# Python has some reeally handy functions such as filter and map
# filter will apply a function to a collectino to filter only those members matching the function

# map will apply a function to every member of a collection
# use case: make sure all our string values are consistently lower case
fruits = ['apple', 'Pear', 'KIWI', 'DuRIan']

# we need to make sure they are all lower case
lower_fruit = tuple( map(str.lower, fruits) ) # here we use the map object to populate a new collection
print(lower_fruit)

# map can be useful to extract from a collection
# here we take just hte first letter of the strings in 'fruits'
result = list( map(lambda s:s[0], lower_fruit) )
print(result)

# here is a utility function
def tidyUp(n):
    ' make sure we have a string with no whitespace'
    if type(n)==str:
        result = n.strip() # remove any whitespace
    else:
        result = 'default'
    return result

values = ['   Python', '    tab', 'done     ']
cleaned_data = list(map(tidyUp, values))
print(cleaned_data)
