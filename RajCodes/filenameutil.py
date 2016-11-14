def extractextension(inputstring):
	outputlist=[]
	l=len(inputstring)
	n=range(0,l)
	for index in range(0, l):
		if inputstring[index] == ".":
			return inputstring[index + 1:]
	
	return ""

print extractextension("sringutil.py")
