# Capatilizing each word in a
x=lambda a : map(lambda z: z.capitalize(), a)
y=["hey this is zaid","i am from hyderabad","this program is short"]

c=list(map(lambda v:' '.join(v),(map(x,list(map(lambda s:s.split(),y))))))

print(c)



