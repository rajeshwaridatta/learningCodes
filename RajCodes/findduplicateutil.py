def swapElements(i,j,numlist):
	temp=numlist[i]
	numlist[i]=numlist[j]
	numlist[j]=temp

def ifDuplicate(numlist):
	for start in range(0, len(numlist)):
		minIndex=start
		for index in range(start,len(numlist)):
			if numlist[minIndex]>numlist[index]:
				minIndex=index
		swapElements(start,minIndex,numlist)


	for start in range(0, len(numlist)-1):
 	  if numlist[start]==numlist[start+1]:
        	 return True
	return False



print ifDuplicate([5,2,6,7,9,13,78])

def ifDuplicatev2(numlist):
	d = {}
	# value -> index
	for index in range(0, len(numlist)):
		key = numlist[index]
		# check if key is present in dictionary
		if key in d:
			return True
		d[key] = 0
	return False

print ifDuplicatev2([10,14,45,12])


scoreList = [14,24,56,65,14,45,56]

# score -> number of occ

def freqDist(numList):
	numDict = {}
	for e in numList:
		if e in numDict:
			# Occ = occurrences already found + 1
			numDict[e] = numDict[e]+1 
		else:
			numDict[e] = 1
	print numDict
freqDist([14,24,56,65,14,45,56])

def freqDistV2(numList):
	numDict = {}
	for e in numList:
		# increment the number if present otherwise set 1
		try:
			numDict[e] += 1
		except KeyError:
			numDict[e] = 1
	print numDict
freqDistV2([14,24,56,65,14,45,56])

