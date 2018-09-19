'''
You can define your own Functions and Methods in Python.
And then call them whenever you need them to be executed.
'''


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

# More functions to practice:

def old_macdonald(name):
    # Capitalises first and fourth letters in a name
    newname = list(name)
    newname[0] = newname[0].capitalize()
    newname[3] = newname[3].capitalize()
    return ''.join(newname)


print(old_macdonald('\nmacdonald') + '\n')

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
        return (smaller(a, b))
    else:
        return (greater(a, b))


print(lesser(2, 4))
print(lesser(2, 5))

# ----------------------------------------------

def summer_69(arr):
    '''
    Summs up numbers in an array, but those between 6 and 9
    and ommitting 6 and 9 too
    if those are present in the array
    '''
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

