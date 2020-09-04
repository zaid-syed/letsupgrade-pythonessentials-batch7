
# day3-batch7-assignment2-python-letsupgrade

for prime in range(1,201):
	count=0
	for n in range(1,prime+1):
		if prime%n==0:
			count+=1
	if count==2:
		print(prime)			
			