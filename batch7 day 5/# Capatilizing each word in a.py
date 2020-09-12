# Capatilizing each word in a
x=lambda a : map(lambda z: z.capitalize(), a)
y=["hey this is shoaib","i am from hyderabad","this program is a little complex"]

c=list(map(lambda v:' '.join(v),(map(x,list(map(lambda s:s.split(),y))))))

print(c)



