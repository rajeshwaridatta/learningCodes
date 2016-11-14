
from mathutil import sigmoid

def isEmpty(l):
	return len(l) == 0

def sigmoidOfList(numberList):
	outputList = []
	while isEmpty(numberList) == False:
		e = numberList.pop(0)
		s = sigmoid(e)
		outputList.append(s)
	return outputList

def sigmoidOfListV2(numberList):
	outputList = []
	for e in numberList:
		s = sigmoid(e)
		outputList.append(s)
	return outputList

resultList = sigmoidOfList([10, 20, 30])
print resultList
resultListV2 = sigmoidOfListV2([10, 20, 30])
print resultListV2

def findDigitsV2(x):
	digits = 0
 	while x > 0:
		digits = digits + 1
		x = x / 10
	return digits

def findDigits(x):
	if x > 0:
		return 1 + findDigits(x/10)
	return 0


print findDigits(1784)
print findDigitsV2(1784)


