
def reversestring():
	stringInput=raw_input("Enter the string: ")
	string = list(stringInput)
	l=len(string)
	for i in range(0,l/2):
		temp = string[i]
		string[i]=string[l-1-i]
		string[l-1-i]=temp
	return "".join(string)

def reversestringslow():
	stringInput=raw_input("Enter the string: ")
	outputString = ""
	for character in stringInput:
		outputString = character + outputString 
	return outputString

#print reversestring()

def printfuction(number):
	outputlist=[]
	i=0
	while i+1<=number:
		
		if i%2==0:
			outputlist.append(0)
		else:
			outputlist.append(1)
		i=i+1
	#print outputlist
#printfuction(5)

def sumoflists(listOfListOfNumbers):
	n=len(listOfListOfNumbers)
	sumoutput=0
	for i in range(0,n):
		eachInnerList = listOfListOfNumbers[i]
		for ele in eachInnerList:
			sumoutput=sumoutput+ele
	return sumoutput


#print sumoflists([[1,2],[3,4]])

def indexOfMatrix(listoflist):
	
	l=len(listoflist)
	numberofrows=l
#assuming that the number of elements in each inner list i s same
	
	numberofcolumns=len(listoflist[0])
		
	print numberofrows
	print numberofcolumns
#indexOfMatrix([[2,3]])

def vowelOrConsonant():
	char=raw_input("Enter the letter: ")
	listofvowel=["a","e","i","o","u"]
	if char in listofvowel:
		print "true"
	else:
		print "false"
#vowelOrConsonant()

def isVowelPresent(string):
	listofvowels=["a","e","i","o","u"]
	for char in string:
		print char
		if char in listofvowels:
			return True
	return False

charac=raw_input("Enter the list of letters: ")
print isVowelPresent(charac)
def evenNum(string):
	l=len(string)
	for e in string

		if e%2==0:
			return True
	return False

def indexofEven(numList):
	outputlist=[]
	for index in range(0,len(numList)):
		e = numList[i]
		if e%2==0:
			outputlist.append(i)
	return outputlist

