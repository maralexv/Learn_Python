''' Inheretance is the ability to use earlier created Classes in the new code'''


class Animal:

    def __init__(self):
        print('ANUMAL CREATED')

    def who_am_i(self):
        print('I am an Animal')

    def east(self):
        print("I am eating")


class Dog:

    def __init__(Animal):
        Animal.__init__
        print('DOG CREATED')

myanimal = Animal()

mydog = Dog()


