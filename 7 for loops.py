# FOR LOOPS

"""
For Loop is used for iterating over a sequence 
(that is either a list, a tuple or a string).
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) # note identation


# break statement we can stop the loop before it has looped through all the items
print ("with 'break' statement")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana": # this will stop the loop at 'banana'
    break
  print(x)

""" 
continue statement we can stop the current iteration of the loop, 
and continue wit the next
"""
print ("with 'continue' statement")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana": # this will skip 'banana'
    continue
  print(x)

"""
To loop through a set of code a 
specified number of times, we can use the range() function.
"""
print("looping through a range")
for x in range(6): # note that range(6) will loop through the values 0 to 5 (!!)
  print(x)


"""
The range() function defaults to 0 as a starting value, however it 
is possible to specify the starting value by adding a parameter: 
range(2, 6), which means values from 2 to 6 (but not including 6)
"""
print("looping through a range, strating from 2")
for x in range(2, 6):
  print(x)

"""
The range() function defaults to increment the sequence by 1, 
however it is possible to specify the increment value by adding 
a third parameter: range(2, 30, 3)
"""
print("looping through a range, starting from 2, but also with increments of 3")
for x in range(2, 30, 3):
  print(x)


"""
Recursion is a common mathematical and programming concept. 
It means that a function calls itself. This has the benefit 
that you can loop through data to reach a result.
"""

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results")
tri_recursion(6)






