def num(a,b):
	i=0
	for bum in a:
		if a[i:i+len(b)]==b:
			print("it's a match")
			return 		
		i=i+1
	print("it's gone")
x=input("enter list elements with spaces in between.")
x=[int(i) for i in x.split()]
y=[1,1,5]
num(x,y)
