# -*- coding: utf-8 -*-


# %s converts everything into STRING:
print("I want to print %s here and %r there" %('something', 'more'))

# %r converts everythign into REPRESENTATION of a STRING:
print('here is a %s number and an %r representation of a string' %(3.14159, 3.14159))

# %d TRUNCATES into integers:
print('Truncating floating point numbers: %d' %(13.9876))

# %f for floating - indicates (total digits to print).(digits after decimal):
print('First: %s, Second: %5.2f, Third: %r' %('hi!', 3.14159, 'bye!'))

#format methid:
print('This is a string with an {}'.format('insert'))

# Inserted objects can be called by index position:
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))

# Inserted objects can be assigned keywords:
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1, b='Two', c=12.3))

# Inserted objects can be reused, avoiding duplication:
print('A %s saved is a %s earned.' %('penny','penny')) # vs.
print('A {p} saved is a {p} earned.'.format(p='penny'))

print('This is my ten-character, two-decimal number:{0:10.2f}'.format(13.579))



"""
For more information on the string .format() method visit 
https://docs.python.org/3/library/string.html#formatstrings

"""

# f-literal:

name = 'Fred'
print(f"He said his name is {name}.")

num = 23.45678
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")  # vs.
print("My 10 character, four decimal number is:{0:10.4f}".format(num))

"""
For more info on formatted string literals visit 
https://docs.python.org/3/reference/lexical_analysis.html#f-strings

"""
