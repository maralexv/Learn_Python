# Lists, Tuples, Sets, Dictionaries


# LISTS

""" 
Method		Description
append()	Adds an element at the end of the list
clear()		Removes all the elements from the list
copy()		Returns a copy of the list
count()		Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()		Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()		Removes the element at the specified position
remove()   	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()		Sorts the list

"""

print("\nLists")

[1,2,3,]
[1,2,3,]+[4,5,6]

# Defining List
thislist = ["apple", "banana", "cherry"]
print(thislist)
# Another way of defining a list
L = list('spam') #creates a list of characters form string
print(L)
# Changing 2nd element of the list
thislist[1] = "blackcurrant"
print(thislist)

# Another way to define a List
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Add element to the end of the List
thislist.append("damson")
print(thislist)

# Insert an element in the list in defined position
thislist.insert(1, "orange")
print(thislist)

# Reverse the list
thislist.reverse()
print(thislist)

# Sort the list items
thislist.sort()
print(thislist)

# Remove specific element from the List
thislist.remove("banana") # removes item with specific value
print(thislist)
thislist.pop(0) # removes item in specific position
print(thislist)

# Length of the List
print(len(thislist))

# Counnnt how many times an item of particular value appears in the list
print(thislist.count('orange'))

# Nested Lists:
thislist.append(L)
print(thislist)

matrix = [[1,2,3,],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[1])
print(matrix[2][2])
print(matrix[:2])



# TUPLES
print("\nTuples")

# Defining Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Printing an item of the Tuple
print(thistuple[0]) # prints the 1st item in the Tuple
print(thistuple[2]) # prints the 3rd item in the Tuple

# Another way to define Tuple
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Length of Tuple (number of items in the Tuple)
print(len(thistuple))

# Tuple unpacking
a, b, c = thistuple
print(a, b, c)



# SETS
print("\nSets")

# Define a Set
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Adding items to Set
thisset.add("damson") #note method 'add' instead of 'append' for Lists
print(thisset)

# Removing items form set
thisset.remove("banana")
print(thisset)

# Determining the length of Set (number of items in Set)
print(len(thisset))



# DICTIONARIES
print("\nDictionaries")

# Defining Dictionary. Note keys and vaues.
mydict =	{
  "apple": "green",
  "banana": "yellow",
  "cherry": "red"
}
print(mydict)

# Changing value of one item (key) in the Dictionary
mydict["apple"] = "red"
print(mydict)

# Anther way to define Dictionary
thisdict =	dict(apple="green", banana="yellow", cherry="red")
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
# note one round-brackets instead of double
print(thisdict)

# Adding Item
thisdict["damson"] = "purple" # note no need to use any method to add to Dictionary
print(thisdict)

#Removing items from Dictionary
del(thisdict["banana"]) # note 'del' command
print(thisdict)

# Getting the length of a Dictionary (number of element in a Dictionary)
print(len(thisdict))

# Nested Dictionaries
thisdict["dict"] = mydict
print(thisdict)
