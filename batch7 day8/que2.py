# batch7 day8 question2
fileHandle=open("Example.txt","r")
print("Reading contents of the file....\n",fileHandle.read())
try:
	fileHandle.write("I want to add this text in the file")
except:
	print("File can not be written in, it is open with read only."