
def findNumRows(matrix):
	return len(matrix)

def findNumCols(matrix):
	if len(matrix) > 0:
		return len(matrix[0])
	else:
		return 0

def askUserMatrix():
	numRows = int(raw_input("Enter the number of rows: "))
	numCols = int(raw_input("Enter the number of cols: "))
	matrix = []
	for i in range(0, numRows):
		matrix.append([])
		for j in range(0, numCols):
			element = int (raw_input("Enter the number [" +str(i) + ", " + str(j) + "]"))
			matrix[i].append(element)
	return matrix
	
def transposeMatrix(matrix):
	transposed=[]
	if len(matrix)>0:
		transrow=len(matrix[0])
		transcol=len(matrix)
		for i in range(0,transrow):
			transposed.append([])
			for j in range(0,transcol):
				transposed[i].append(matrix[j][i])
	else:
		return []
	return transposed

#inputMatrix = askUserMatrix()
#print(inputMatrix)
#print transposeMatrix(inputMatrix)
def diagonalmatrix(matrix):
	#all nondiagonal elements are zero
	for i in range(0, findNumRows(matrix)):
		for j in range(0, findNumCols(matrix)):
			if isdiagonal(i,j)==False and matrix[i][j]!=0:
				return False
	return True

	#if any of the non diagonal element is not zero then return non diagonal


def isdiagonal(i,j):
	if i==j:
		return True
	else:
		return False

