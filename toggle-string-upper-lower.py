# Toggle String: String S is consisting of uppercase and lowercase English alphabets. 
# The script needs to change the case of each alphabet in this String. 

s = 'aBcdE'

result = ""
for c in s:
	if c.islower():
		result += c.upper()
	else:
		result += c.lower()

print(result)