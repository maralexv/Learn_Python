# Conditional Branching (IF)

print("Hi, what's your name?")
name = input()
print("So, " + name + ", we shall play a little game...")
print("you will give me two numbers and I will tell you which one is greater.")
print("Ready?")
ready = input()

if ready == "no" or ready == "No" or ready == "Nope" or ready == "nope" or ready == "n" or ready == "N":
    print("Ok, good bye, " + name + "!")
    print("See you next time reoud...")

else:
    print("Give me your 1st number please:")
    a = input()
    print("Now give me your second number:")
    b = input()

    if b > a:
        print(name + ", your 2nd number (" + b + ") is greater than your 1st one (" + a + ")")  # note identation
        print("See you later ," + name)
    elif a == b:
        print("Ha! Your numbers are equal. This was easy, " + name)  # note identation
        print("Am I not good?! :)")
        print("Hasta la vista!")
    else:
        print(name + ", this time the 1st number (" + a + ") is greater than the 2nd (" + b + ")")  # note identation
        print("Good bye ," + name + "!")
