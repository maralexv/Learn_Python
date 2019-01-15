
def prime(given_number):
	'''
	Builds a list of prime numbers up to given number
	'''
	if given_number < 2:
		print ('By definition, Prime numnbers are positive whole \
			numbers and 1 is not Prime')
		return []
	# Initiate the list
	primeslist = [2]
	possibleprime = 3
	# Check if Prime
	while possibleprime <= given_number:
		for num in primeslist:
			if possibleprime%num==0:
				possibleprime += 2
				break
		else:
			primeslist.append(possibleprime)
			possibleprime += 2
	return primeslist
	
# test by outputting the result (mark as comment if and when not needed)
print(prime(99))


# Another way of doing it:

def isprime(n):
	''' Check if any given positive number is divisable by any 
	preceeding positive number (that is greater than 1)''' 
	for x in range(2,n):
		if n%x == 0:
			return False
	#And mark as Prime, if not:
	return True

def primes_list(given_n):
	''' Build the list of prime numbers, using 'isprime' function'''
	return [str(x) for x in range(2,given_n+1) if isprime(x)]

# test by outputting the result (mark as comment if and when not needed)
result = ' '.join(primes_list(99))
print(result)


# Another way of doing it:

def isprime2(n):
	''' Check if any given positive number is divisable by any 
	preceeding positive number (that is greater than 1)''' 
	for x in range(2,int((n)**(1/2)+1)):
		if n%x == 0:
			return False
	#And mark as Prime, if not:
	return True

def Primes_list2(given_n):
	''' Build the list of prime numbers, using 'isprime' function'''
	return [x for x in range(2,given_n+1) if isprime2(x)]

# test by outputting the result (mark as comment if and when not needed)
print(Primes_list2(99))

