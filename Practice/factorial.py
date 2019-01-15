# FACTORIAL

def myfactorial(n):
	if n < 2:
		return 1
	else:
		return  n * myfactorial(n - 1)

print (myfactorial(5))

