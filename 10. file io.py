#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 14:32:50 2018

@author: Alex
"""


"""
open() returns a file object, and is most commonly used with two 
arguments: open(filename, mode). f is a variable here:

>>> f = open('workfile', 'w')

The first argument is a string containing the filename. 
The second argument is another string containing a few characters 
describing the way in which the file will be used. mode can be 'r' when 
the file will only be read, 'w' for only writing (an existing file with 
the same name will be erased), and 'a' opens the file for appending; any
data written to the file is automatically added to the end. 'r+' opens 
the file for both reading and writing. The mode argument is optional; 
'r' will be assumed if it’s omitted.

"""

myfile = open('my_file.txt', 'w')


"""
myfile.write(string) writes the contents of string to the file, returning 
the number of characters written. "\n" is a cmmand to move to next line.

>>> myfile.write('This is a test\n')

"""

myfile.write('This is a test\nIt is my first file with Python\nLine 1\n')  # Write into the file

myfile.close() # need to close file after use


"""
To read a file’s contents, call f.read(size), which reads some quantity 
of data and returns it as a string (in text mode) or bytes object (in 
binary mode). size is an optional numeric argument. When size is 
omitted or negative, the entire contents of the file will be read and 
returned; it’s your problem if the file is twice as large as your 
machine’s memory. 

"""

myfile = open('my_file.txt') 	# r mode is assumed, when ommitted
print(myfile.read())			# python has read file and is at the end of it
myfile.seek(0)					# need to move back to beginning (position 0)
read_file_data = myfile.read()
print (read_file_data)
myfile.read()					# returns a string of 10 initial characters from the file
myfile.readlines()				# returns a list of strings, each representing 
								# a single line of the file. If n (10 in this example) 
								# is not provided then all lines of the file are
								# returned. If n is provided then n characters are read
								# but n is rounded up so that an entire line is returned.

myfile.close()

"""
It is good practice to use the with keyword when dealing with file 
objects. The advantage is that the file is properly closed after its 
suite finishes, even if an exception is raised at some point. No need 
to f.close()

>>> with open('workfile') as f:
...     read_data = f.read()

"""

with open('my_file.txt') as f:
	read_file_data = f.readlines()
	print (read_file_data)


with open('my_file.txt', 'a+') as f:	# 'a+' = open in 'append' mode
	for line in range (2,11):
		f.write(f'line {line}\n')

with open('my_file.txt') as f:
	print(f.read())


"""
Python allows you to use the popular data interchange format called JSON
(JavaScript Object Notation). The standard module called json can take 
Python data hierarchies, and convert them to string representations; 
this process is called serializing. 

Note The JSON format is commonly used by modern applications to allow 
for data exchange. Many programmers are already familiar with it, which 
makes it a good choice for interoperability.

If you have an object x, you can view its JSON string representation 
with a simple line of code:


>>> import json

>>> json.dumps([1, 'simple', 'list'])
'[1, "simple", "list"]'

"""

import json

content={'node1': [1,'SIMPLE',2.34,'list']}

file = open('my_json_file.json', 'w')
json.dump(content, file)
file.close()

with open('my_json_file.json') as f:
	print(f.read())

'''
simple manipulations woth the content of the file
'''

with open('my_file.txt') as f:
	num_lines = len(f.readlines())
	f.seek(0)	# need to return to the start of the file	
	num_char = len(f.read())
	print(f'The number of characters in the file is {num_char}\nAnd the number of lines is {num_lines}.')

'''
Working with .csv files
'''

olympians = [("John Aalberg", 31, "Cross Country Skiing, 15KM"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

with open('olymp.csv', 'w') as f:
	csv_header = 'Name,Age,Sport'
	f.write(csv_header)
	f.write('\n')
	for el in olympians:
		csv_row = '{},{},{}'.format(*el)
		f.write(csv_row)
		f.write('\n')

