# even numbers between 0 and 10
result = [num for num in range(11) if num % 2 == 0]
for x in result: print(x)

print('\n')

#  numbers between 1 and 50, divisable by 3
result = [num for num in range(1, 51) if num % 3 == 0]
print('{}'.format(result))

print('\n')

# 'Print every word in this sentence that has an even number of letters'
st = 'Print every word in this sentence that has an\
 even number of letters'

for word in st.split():
    if len(word) % 2 == 0:
        print(word)

# FizzBuzz Test
print('\nFizzBuzz test:')

mylist = [x for x in range(1, 101)]
for i in mylist:
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# 'Create a list of the first letter of every word of this string'

s = 'Create a list of the first letter of every word of this string'

# strait forward solution:
newlist = s.split()
result = [newlist[i][0] for i in range(len(newlist))]
print(f'\n{result}')

# better solution:
result2 = [word[0] for word in s.split()]
print(f'{result2}\n')


# -------------------------------------------------------------------

# FUNCTIONS

def myfunc(name='NAME'):
    print(f'My name is {name}')


myfunc('Alex')


# *args acts like a wild card for arguments:

def myfunction(*args):
    '''
    square root of the sum of the arguments
    '''
    return sum((args)) ** (1 / 2)  # 'args' are items in a tuple


# a little practice with output formating:

print('%.3f' % myfunction(1, 2, 3, 4, 5, 6, 7, 8, 9, ) + ' <-- no idenation')
print('%1.3f' % myfunction(1, 2, 3, 4, 5, 6, 7, 8, 9, ) + ' <-- idenation 1')
print('%2.3f' % myfunction(1, 2, 3, 4, 5, 6, 7, 8, 9, ) + ' <-- idenation 2')
print('%3.3f' % myfunction(1, 2, 3, 4, 5, 6, 7, 8, 9, ) + ' <-- idenation 3')
print('%4.3f' % myfunction(1, 2, 3, 4, 5, 6, 7, 8, 9, ) + ' <-- idenation 4')
print('%5.3f' % myfunction(1, 2, 3, 4, 5, 6, 7, 8, 9, ) + ' <-- idenation 5')
print('%6.3f' % myfunction(1, 2, 3, 4, 5, 6, 7, 8, 9, ) + ' <-- idenation 6')
print('%10.3f' % myfunction(1, 2, 3, 4, 5, 6, 7, 8, 9, ) + ' <-- idenation 10')
print('%15.3f' % myfunction(1, 2, 3, 4, 5, 6, 7, 8, 9, ) + ' <-- idenation 15\n')


# ---------------------------------------------------------

def smaller(a, b):
    if a < b:
        return a
    else:
        return b


def greater(a, b):
    if a < b:
        return b
    else:
        return a


def lesser(a, b):
    if a % 2 == 0 and b % 2 == 0:  # check if both are even
        return smaller(a, b)
    else:
        return greater(a, b)


print(lesser(2, 4))
print(lesser(2, 5))


# ---------------------------------------------------------


def old_macdonald(name):
    # Capitalises first and fourth letters in a name
    newname = list(name)
    newname[0] = newname[0].capitalize()
    newname[3] = newname[3].capitalize()
    return ''.join(newname)


print(old_macdonald('\nmacdonald') + '\n')


def master_yoda(sentence):
    # Reverses the words in a sentence
    return ' '.join(sentence.split()[::-1])


print(master_yoda('I am home'))
print(master_yoda('We are ready') + '\n')


def peper_doll(word):
    # Replaces each letter os a word with 3 identical letters
    return ''.join(x * 3 for x in list(word))


print(peper_doll('Hello'))
print(peper_doll('Yesterday'))
print(peper_doll('Hello Yesterday') + '\n')


def summer_69(arr):
    """
    Summs up numbers in an array, but those between 6 and 9
    and ommitting 6 and 9 too
    if those are present in the array
    """
    stop = 0  # define variable
    start = 0  # define variable
    if 6 or 9 in arr:
        for i in range(len(arr)):
            if arr[i] == 6:
                stop = i
            elif arr[i] == 9:
                start = i + 1
        return sum(arr[:stop]) + sum(arr[start:])
    return sum(arr)


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 8, 9]))
print(f'{summer_69([2,1,6,9,11])} \n')

# iterating through list:

print('These two codes will produce the same result:\n')

print('Code1\n')

mylist = [1, 2, 3, 6]
for x in range(len(mylist)):
    print(mylist[x])

print('\nCode2\n')

mylist = [1, 2, 3, 6]
for x in mylist:
    print(x)

print('\n')

# --------------------------------------------------

'''
Write a function that takes in a list of integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False
'''


def bond(arr):
    result = False
    worklist = []
    for item in range(len(arr)):
        if arr[item] == 0 or arr[item] == 7:
            worklist.append(arr[item])
    for el in range(len(worklist)):
        if (worklist[el:el + 3]) == [0, 0, 7]:
            result = True
    return result


print(bond([1, 2, 4, 0, 0, 7, 5]))
print(bond([1, 0, 2, 4, 0, 5, 7]))
print(bond([1, 7, 2, 0, 4, 5, 0]))




# -------------------------------------------------

# Build an array of prime numbers up to a cetain numnber:


def check_if_prime(num):

    for x in range(2, int(num ** (1 / 2) + 1)):
        if num % x == 0:
            return False
    return True


def list_of_primes(x):
    return [n for n in range(2, x + 1) if check_if_prime(n)]


print(list_of_primes(20))
print('\n')



""" Count the number of primes: function that returns the
number of prime numbers that exist up to and including a
given numbe """

def check_if_prime2(num):
    """ Checks if a given number is a Prime Number """
    for x in range(2, int(num ** (1 / 2) + 1)):
        if num % x == 0:
            return False
    return True


def number_of_primes2(x):
    """ Counts the number os Primes between 2 and Given Number """
    return len([n for n in range(2, x + 1) if check_if_prime2(n)])


print(f'{number_of_primes2(100)}\n')

# --------------------------------------------------


# Classes and Methods:

class Circle():
    # CLASS OBJECT ATTRIBUTE:
    pi = 3.14159

    # INSTANCE ATTIRUTES
    def __init__(self, radius=1):
        self.radius = radius
        self.circum = 2*self.radius*Circle.pi

    # METHOD
    def circle_surface(self):
        return Circle.pi*(self.radius**2)


my_circle = Circle(3)

print('%0.2f\n' % my_circle.circle_surface())


''' ---------- Practice Classes ---------- '''

# Method to calculate the volume and surface area of a cilinder:


class Cylinder():

    # CLASS OBJECT ATTRIBUTE
    pi = 3.14159

    # INSTANCE ATTIRUTES
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def surface_area(self):
        return 2*Cylinder.pi*self.radius**2 + 2*Cylinder.pi*self.radius*self.height

    def volume(self):
        return self.height*Cylinder.pi*self.radius**2


c = Cylinder(2, 3)
print('%0.2f' % c.volume())
print('%0.2f\n' % c.surface_area())


class Line():

    # INSTANCE ATTIRUTES
    def __init__(self, dot1=(0, 0), dot2=(0, 0)):
        self.dot1 = dot1
        self.dot2 = dot2

    # METHODS
    def distance(self):
        return ((self.dot2[1]-self.dot1[1])**2 + (self.dot2[0]-self.dot1[0])**2)**(1/2)

    def slope(self):
        return (self.dot2[1]-self.dot1[1])/(self.dot2[0]-self.dot1[0])


d1 = (3, 2)
d2 = (8, 10)

li = Line(d1, d2)

print('%10.3f' % li.distance())
print(li.slope())


""" --------- Bank Account Class ------------"""


class BankAccount():

    # INSTANCE ATTIRUTES
    def __init__(self, client = "Name Surname", currency = "€", balance = 0.0):

        self.client = client
        self.currency = currency
        self.balance = balance

    # METHODS
    def checkacc (self):

        print("\nAccount Name: {};\nAccount balance: {}{:0.2f};\n".format(self.client, self.currency, self.balance))

    def deposit (self):

        amount = float(input(f"{self.client}, how much would you like to deposit? "))
        self.balance = self.balance + amount
        print (f"The amount {self.currency}{amount} has been added to your account.\n")

    def withdraw (self):

        amount = float(input(f"{self.client}, how much would you like to withdraw? "))
        if self.balance < amount:
            print(f"Sorry, you do not have enough funds on the account for this transaction.\n")
        else:
            self.balance = self.balance - amount
            print(f"The amount {self.currency}{amount} has been withdrawn from your account.\n")
            print(f"The available balance on your account is {self.currency}{self.balance}")


    # SPECIAL METHOD THAT ALLOWS PRINTING OF THE OBJECT
    def __str__ (self):
        return "\nAccount Name: {};\nAccount balance: {}{:0.2f};\n".format(self.client, self.currency, self.balance)



a = BankAccount("Alex Marchenko")
print (a)
a.deposit()
a.withdraw()
print(a)
a.withdraw()
print(a)
a.checkacc()

# --------------------------------------------------

# FIBONNACCI NUMBERS:
def fibonnacci (n):
    a = 0
    b = 1
    for item in range(n+1):
        yield a
        a, b = b, a + b


# SPLIT DOMAIN FORM E-MAIL:
email = 'name.surname@domain.com'
print(email.split("@"))

# FACTORIAL
def factorial(n):
    if n < 2:
        return 1
    else:
        return  n * factorial(n - 1)

print(factorial(5))
