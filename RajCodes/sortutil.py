def selectionSort(numList):
	for start in range(0, len(numList)):
		minIndex = start
		for index in range(start, len(numList)):
			if numList[minIndex] > numList[index]:
				minIndex = index
		swapElements(start,minIndex,numList)
	return numList

def swapElements(i, j, numList):
	temp = numList[i]
	numList[i] = numList[j]
	numList[j] = temp

def isSorted(numlist):
	for i in range(0,len(numlist)):
		if numlist[i]>numlist[i+1]:
			return False
	return True

print isSorted([3,6,1,45,87])
