# Generator is a function that yields results rather that returning them
# It is much more memory efficietn in case you do not need to keep a list
# or tuple of results, bu tonly need a result at a time/step
# built-in functon range() is such a generator.
# Key-word yield is used to greate generators.

# EXAMPLE
def fibonnacci (n):
    a = 0
    b = 1
    for item in range(n+1):
        yield a
        a, b = b, a + b

# ONE WAY OF GETTING OUTPUT (not memeory efficient)
print(list(fibonnacci(10)))

# ANOTHER WAY OF GENERATING OUTPUT (more memory efficient)
# BUT THIS WILL NOT BE VISIBLE< ONLY STORRD IN MEMORY
print(fibonnacci(10))

# SAME RESULT, BUT VISIBLE:
for i in fibonnacci(10):
    print (i)
