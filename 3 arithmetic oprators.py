# Arithmetic operators

print("3+2")
print(3+2)
print("16/4")
print(16/4)
print("5*7")
print(5*7)
print("12%5")
print(12%5)
print("13%4")
print(13%4)
print("18%8")
print(18%8)
print("12//5")
print(12//5)
print("13//4")
print(13//4)
print("18//8")
print(18//8)
print("2**3")
print(2**3)


# MEMBERSHIP OPERATORS

x = ["apple", "banana"]
print("banana" in x) # returns True becasue "banana" is in the list

x = ["apple", "banana"]
print("pineapple" not in x) # returns True because "pineapple" is not in the list


# Identity operators

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # returns True because z is the same object as x

print(x is y) # returns False because x is not the same object as y, even if they have the same content

# to demonstrate the difference betweeen "is" and "==":
print(x == y) # this comparison returns True because x is exactly equal to y




