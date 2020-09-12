def prime(givenNumber):
	count=0
	for variableInIterable in range(1,givenNumber+1):
		if givenNumber%variableInIterable==0:
			count=count+1
	if count==2:
		return True
	else:
		return False
primeNumber=(filter(prime,range(1,2500)))
print("The following are prime numbers from 1 to 2500 using filter")
for eachElement in primeNumber:
	print(eachElement)