numbers = [2,5,4,3,2,5,6,4,32,4,3,234,3,22,5,6,89,7,8,6,8,7,8]

def findMaxOccuringNumber(numList):
	dictionary = {}
	for e in numList:
		if e in dictionary:
			dictionary[e] += 1
		else:
			dictionary[e]=1
	
	# maxkeys are numbers having all maxVal number of occurrences.
	maxVal = None
	maxKeys = []
	for key in dictionary:
		numOcc = dictionary[key]
		if len(maxKeys) == 0:
			maxKeys = [key]
			maxVal = numOcc
		elif maxVal < numOcc: # found a new number which has higher occ
			maxVal = numOcc
			maxKeys = [key]
		elif maxVal == numOcc:
			maxKeys.append(key)
	return maxKeys

print findMaxOccuringNumber(numbers)
			
