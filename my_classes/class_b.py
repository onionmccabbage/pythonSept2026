# more involved custom class: a person has a name and an age
# name must be a non-empty string
# age integer greater than 13


class Person():
    '''store a persons name ensuring it is a non-empty string
    Also store age as an integer greater than 13'''
    def __init__(self, name, age):
        # this is the initialize function: it runs once EVERY time we create a new instane
        self.name = name
        self.age  = age
    # we can write get-set methods for the name
    @property # can only apply to a SINGLE property
    def name(self):
        # class properties with a leading underscore are called 'name mangling'
        return self.__name # this value is not accesssible outside the class instance
    @name.setter
    def name(self, new_name):
    # the validation bit
        if type(new_name) == str and len(new_name) >0:
            self.__name = new_name
        else:
            raise TypeError(f'{new_name} is not a valid value (must be a string)')
    # getter and setter for the age property
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, new_age):
        # here we carry out validation
        if type(new_age) == int and new_age>13:
            self.__age = new_age # name-mangle this value
        else:
            raise TypeError('Age must be an integer greater than 13')


if __name__ == '__main__':
    #make instanves of our Person class
    Ada = Person('Ada', 99)
    Beth = Person('Beth', 14)
    print(Ada.name)
    try:
        Floella = Person(True, 66) # this will fail
    except TypeError:
        pass # not a good solution!!!