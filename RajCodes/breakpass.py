

def negativePresentInMatrix(matrix):
	for row in matrix:
		for e in row:
			if e<0:
				return True
	return False

def foo(matrix):
	output = []
	for row in matrix:
		rowOutput = False
		for e in row:
			if e<0:
				rowOutput = True
				break
		output.append(rowOutput)
	return output

m = [[1,2,3, 0, 0, 0], [2,-6,0, 0, 0, 0], [1,6,-1, 0, 0, 0]]

eo = [False,True,True]

ao = foo(m)
print ao

def removeChar(string, n):
	oString = ""
	for index in range(0, len(string)):
		if index == n:
			continue
		oString +=string[index]
	return oString

print removeChar("bhuban", 2)

