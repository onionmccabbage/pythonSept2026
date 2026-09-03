# end = 'go'

# while end !='stop':
#     ask = input('gimme summat: ')
#     print(type(ask))
#     print(int(float(ask)))
#     end = ask

# why do we need classes? (custom objects)
# got numbers
a=3
b=7.6
# got text
s ='who needs a class!!!!'
# list, tuple, dict, set, range, gen, filter....

print(type([]))

# There is an emerging fashion for type hinting across modern programming languages
def fn()->str: # the ->str bit is a type hint: this function is meant to return a string
    return '1'

print(  fn()  )