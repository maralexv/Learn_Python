import random
import csv

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ops_list = ['add', 'sub']

a, b, r, i = 0, 0, 0, 0
operator = ''
rows = []

while i <50:

    a = random.choice(int_list)

    b = random.choice(int_list)

    operator = random.choice(ops_list)


    if a + b < 10:
        continue

    if operator == 'add':
        rows.append([a, '+', b, '='])
    else:
        r = b + a
        rows.append([r, '-', a, '='])

    i = i + 1

"""
for el in rows:
    print (el)
"""

# define scv file
file = 'Po-arithmetics.csv' 

# create and/or open csv file for writing
with open(file, 'w') as f:

    # create csv writer object
    csvwriter = csv.writer(f)

    # write rows into csv file
    csvwriter.writerows(rows)

