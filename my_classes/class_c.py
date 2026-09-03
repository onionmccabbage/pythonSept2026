from class_b import Person

# Classes always inherit
class Admin(Person): # unless we say otherwise, our custom classes inherit from 'object'
    def __str__(self):
        return f'This administrator is {self.name}'


if __name__ == '__main__':
    Xena = Admin('Xena', 345624)
    print(Xena)