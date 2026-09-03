#  more involved custom class


class Person():
    '''store a persons name ensuring it is a non-empty string'''
    def __init__(self, name):
        # this is the initialize function: it runs once EVERY time we create an ew isntane
        self.name = name
    # we van write get-set methods for the name
    @property
    def name(self):
        return self._name # this value is not accesssible outside the class instance
    @name.setter
    def name(self, new_name):
    # the validation bit
        if type(new_name) == str and len(new_name) >0:
            self._name = new_name
        else:
            raise TypeError(f'{new_name} is not a valid value (must be a string)')


if __name__ == '__main__':
    #make instanves of our Person class
    Ada = Person('Ada')
    print(Ada.name)
    Floella = Person(True) # this will fail