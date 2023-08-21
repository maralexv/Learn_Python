import random
import csv

# define the list of numbers for the excercises
int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# define the list of mathematical operators to be used in the excercises
ops_list = ['add', 'sub']

# define variables
a, b, r, i = 0, 0, 0, 0
operator = ''

# define empty list to record the excercises
rows = []

# loop to generate 50 excercises 
while i <50:

    # set a equal to a random mumber for the predefined list for the excercise
    a = random.choice(int_list)

    # set b equal to a random mumber for the predefined list for the excercise
    b = random.choice(int_list)

    # randomly choose mathematical operator for the excercise
    operator = random.choice(ops_list)

    # skip if a + b equals less than 10
    if a + b < 10:
        continue

    # populate the list of excercises
    if operator == 'add':
        rows.append([a, '+', b, '='])
    else:
        r = b + a
        rows.append([r, '-', a, '='])

    # increment counter
    i = i + 1

"""
# print list of excercises
for el in rows:
    print (el)
"""

# output the excercises into an csv file
#  
# define scv file
file = 'Po-arithmetics.csv' 

# create and/or open csv file for writing
with open(file, 'w') as f:

    # create csv writer object
    csvwriter = csv.writer(f)

    # write rows into csv file
    csvwriter.writerows(rows)

