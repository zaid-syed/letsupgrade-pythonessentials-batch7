# day3-batch7-assignment1-python-letsupgrade
altitude= int(input("altitude of plane"))
if altitude<=1000:
	print("safe land")
elif altitude<=5000:
	print("come to 1000")
else:		
	print("go around and try again")

# day3-batch7-assignment2-python-letsupgrade

for prime in range(1,201):
	count=0
	for n in range(1,prime+1):
		if prime%n=0:
			count+=1
	if count==2:
		print(prime)			
			