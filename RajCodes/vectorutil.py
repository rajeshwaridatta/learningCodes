
def magnitudeSquare(vector):
	squaremagnitudeoutput=0
	for i in vector:
		a= math.pow(i,2)
		squaremagnitudeoutput = a + squaremagnitudeoutput
	return squaremagnitudeoutputi
def isEmpty(l):
        return len(l) == 0
import math
def magnitudesquare(vector):
	if isEmpty(vector)==True:
		return 0
	s=vector[0]
	sq= math.pow(s,2)
	restlist=[]
	for e in vector:
		restlist.append(e)
	restlist.pop(0)
	M=magnitudesquare(restlist)+sq
	return M
def summation(vector):
	if isEmpty(vector)==True:
		return 0
	a=vector[0]
	restlist=[]
	for i in vector:
		restlist.append(i)
	restlist.pop(0)
	S=summation(restlist)+a
	return S
def Lengthoflist(list):
	outputlength=0	
	for i in list:
		outputlength=outputlength+1
	return outputlength

def divisibleInputs(a,b):
	if a%b==0:
		return True
	else:
		return False

def inBetweenInputs(a,b):
	outputlist=[]
	while a<b:
		outputlist.append(a)
		a = a+1
	return outputlist

def dotProduct(firstVector, secondVector):
	# Assuming both the input vectors are of the same dimension
	length = len(firstVector)
	dotProductOutput = 0
	for i in range(0, length):
		product = firstVector[i] * secondVector[i]
		dotProductOutput = dotProductOutput + product
	return dotProductOutput

def reversestring():
	stringInput=raw_input("Enter the string: ")
	string = list(stringInput)
	l=len(string)
	for i in range(0,l/2):
		temp = string[i]
		string[i]=string[l-1-i]
		string[l-1-i]=temp
		print string
	return "".join(string)

print reversestring()
