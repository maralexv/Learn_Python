# WHILE LOOP

# while loop executes a set of statements as long as a condition is true.

print("print numbers fomr 1 to 6")
i = 1
while i <= 6:
  print(i) # note identation
  i += 1   # note identation

# using 'break' method
print("break method - break at 3")
i = 1
while i < 6:
  print(i)
  if i == 3: # loop will stop at 3
    break
  i += 1

# using 'continue' statement
print ("with the continue statement we can stop the current iteration, and continue with the next:")
i = 0
while i < 6:
  i += 1 
  if i == 3: # 3 will be skipped
    continue
  print(i)