# map applies a function to all the items in an input_list:
# map(function_to_apply, list_of_inputs)

# one way of doing:
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)

# map way of doing the same:
items = [1, 2, 3, 4, 5]
def square (x):
 	return x*x

squared = list(map(square, items))
print (squared)

# using map with lambda makes code even cleaner (same example as above):
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))


# filter creates a list of elements for which a function return is True
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)