#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 17:28:43 2018

@author: Alex
"""

# creat a list by comprehansion
lst = [x for x in range(10)]
print(lst)

lst = [[x,x/2,x**2] for x in range(1,20,2)]
print (lst)

lst=[ord(x) for x in 'hellow world']
print (lst)



school = 'Massachusetts Institute of Technology'
num_vowels = 0
num_cons = 0

for chara in school:
    if chara == 'a' or chara == 'e' or chara == 'i' \
       or chara == 'o' or chara == 'u':
        num_vowels += 1
    elif chara == 'o' or chara == 'M':
        print(char)
    else:
        num_cons -= 1

print('num_vowels is: ' + str(num_vowels))
print('num_cons is: ' + str(num_cons))
