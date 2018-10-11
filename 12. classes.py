'''
Classes in Python - possibility to define your oen methods.
'''

# Class Example

class Dog ():

    # CLASS OBJECT ATTRIBUTES (THE SAME FOR ANY INSTANCE OF THE CLASS)

    species = 'mammal'

    # Define Instance
    def __init__(self, breed, name, spots):
        # Attributes (attribute_name)
        # We take in the argument
        # Assign it to self.attribute_name
        self.breed = breed
        self.name = name
        self.spots = spots # expexts bulean (True/False)

    # OPERATIONS/ACTIONS --> Methods
    # Methods are the functions inside of a Class

    def bark(self):
        print(f'WOOF! WOOF! my name is {self.name}')

# Here we define new object my_dog with attributes
my_dog = Dog('Buldog', 'Moses', True)

print(type(my_dog))     # Check the type of the newly created object
print(my_dog.species)   # Check one of the attributes of the new object
print(my_dog.name)      # Check another attribute of the new object

my_dog.bark()   # Calls (executes) Method ".bark" on the object my_dog



