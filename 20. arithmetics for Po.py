import random
import csv

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ops_list = ['add', 'sub']

a, b, r, x = 0, 0, 0, 0
operator = ''
rows = []

while x <6:

    a = random.choice(int_list)
    b = random.choice(int_list)
    operator = random.choice(ops_list)

    if a + b < 11:
        continue

    if operator == 'add':
        r = a + b
        rows.append([a, ' + ', b, ' = ', ' ___'])
    elif a >= b:
        r = a + b 
        rows.append([r, ' - ', b, ' = ', ' ___'])
    else:
        r = b + a
        rows.append([r, ' - ', a, ' = ', ' ___'])

    x = x + 1

for el in rows:
    print (el)

