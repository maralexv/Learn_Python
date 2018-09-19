# My first python file

print ("Hello World!")

x = "Awesome"
print ("Python is " + x)

# Numbers

x = 1
y = 3.5656
z = -3255522
a = 1j

print(type(x))
print(type(y))
print(type(z))
print(type(a))

# Strings

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "hello"
print(a[1]) # returns 2nd character(!!)

a = "world"
print(a[2:5]) # returns 3rd through 4th characters

a = "Hello, World!"
print(len(a)) # returns the length of the string

a = "Hello, World!"
print(a.replace("H", "J")) # methond .replace() replaces  characters

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


# Defining the type of a variable

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'


if 6 > 7:
   print("Yep")
