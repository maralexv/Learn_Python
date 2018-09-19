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

f = open('myfile.txt', 'w')


"""
f.write(string) writes the contents of string to the file, returning 
the number of characters written. "\n" is a cmmand to move to next line.

>>> f.write('This is a test\n')

"""

f.write('This is a test\nIt is my first file with Python\nLine 1\n')

f.close() # need to close file after use


"""
To read a file’s contents, call f.read(size), which reads some quantity 
of data and returns it as a string (in text mode) or bytes object (in 
binary mode). size is an optional numeric argument. When size is 
omitted or negative, the entire contents of the file will be read and 
returned; it’s your problem if the file is twice as large as your 
machine’s memory. 

"""

f = open('myfile.txt') 	# r mode is assumed, when ommitted
print(f.read())				# python has read file and is at the end of it
f.seek(0)				# need to move back to beginning (position 0)
read_file_data = f.read()
print (read_file_data)

f.close()

"""
It is good practice to use the with keyword when dealing with file 
objects. The advantage is that the file is properly closed after its 
suite finishes, even if an exception is raised at some point. No need 
to f.close()

>>> with open('workfile') as f:
...     read_data = f.read()

"""

with open('myfile.txt') as f:
	read_file_data = f.read()
	print (read_file_data)


with open('myfile.txt', 'a+') as f:	# open in 'append' mode
	for line in range (2,11):
		f.write(f'line {line}\n')

with open('myfile.txt') as f:
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

L=[1,'SIMPLE',2.34,'list']

file = open('my_json_file.json', 'w')
json.dump(L, file)
file.close()

with open('my_json_file.json') as f:
	print(f.read())


