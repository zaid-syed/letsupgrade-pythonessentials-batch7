# day2-batch7-python-letsupgrade
# Q1.lists and its default functions

do=["wakeup","workout","breakfast","study"]
print(do)
do.append("coffee")
print(do)
do.pop()
print(do)
do.insert(1,"milk")
print(do)
print(do.count("study"))
do.clear()
print(do)
print("\n\n\n") 

# Q2.dictionary and its default functions

kids={1:"zaid",2:"shoaib",3:"saikiran",4:"rao"}
print(kids)
print(kids.values())
kids.copy()
print(kids)
print(kids.items())
print(kids.keys())
kids.clear()
print(kids,"\n\n\n")

# Q3.sets and its default functions

roll={171,173,175,177,179}
print(roll)
roll.add(181)
print(roll)
roll.copy
print(roll)
roll.discard(179)
print(roll)
roll.pop()
print(roll)
roll.clear()
print(roll,"\n\n\n")

# Q4. tuple and explore default methods

mix=("this","is",1,['messed',"up"],("tupleee..."),"is","it")
print(mix)
print(mix.count('is'))
print(mix.index('it'))
print("\n\n\n")

# Q5.strings and explore default methods

s="this is a string"
print(s)
print(s.capitalize())
print(s.upper())
print(s.isalpha())
print(s.isalnum())
print(s.isprintable())
