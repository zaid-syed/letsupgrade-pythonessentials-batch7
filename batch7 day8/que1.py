# batch7 day8 question1
def getStartAndEndPointForList(anyFunc):
	def WrapFunc():
		startPoint=int(input("Enter starting point for list"))
		endPoint=int(input("Enter end point for list"))
		for r in range(startPoint,endPoint+1):
			anyFunc(r)
	return WrapFunc
@getStartAndEndPointForList
def Prime(checkNumber):
	FactorsCount=0
	for n in range(1,checkNumber+1):
		if checkNumber%n==0:
			FactorsCount=FactorsCount+1
	if FactorsCount==2:
		print(checkNumber,"is a prime number")
Prime()