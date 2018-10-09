#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
To avoid code stop executing in case of an error (due to wrong input by a user or another programme),
Python offers Try - Except - Else - Finally framnework.

try – this block of code will try to execute;
except – this block of code will execute ONLY IF there is an ERROR (you can specify error type for each 'except';
else – this will execute IF there is NO ERROR;
finally – this block of code will execute ALWAYS;

"""

arr = [1, 2, 3]

for i in arr:
    try:
        print(i ** 2)
    except:
        print("your input inclides non-numbers, probably strings")

print("I am out of the loop\n")

# One more option:
for i in arr:
    try:
        print(i ** 2)
    except TypeError:   # Indicating specific Error
        print("your input inclides non-numbers, probably strings")

print("I am out of the loop\n")



x = 5
y = 0

try:
    z = x/y
except:
    print("'Y' cannot be '0'\n")
else:
    print(z + "\n")


def ask():
    num = int(input("Please give me a number: \n"))
    return num ** 2

while True:
    try:
        value = ask()
        print(f"Thank you. The square of your number is {value}\n")
        break
    except:
        print ("You have not given me a number. Please try again\n")
        continue

