from matrixutil import askUserMatrix
from matrixutil import findNumRows
from matrixutil import findNumCols

def productMatrix(matrix1, matrix2):
	# ensure the matrices are multipliable
	if findNumCols(matrix1)	!= findNumRows(matrix2):
		return None

	productMatrix = []
	numRowsProductMatrix = findNumRows(matrix1)
	numColsProductMatrix = findNumCols(matrix2)
	for i in range(0, numRowsProductMatrix):
		productMatrix.append([])
		for j in range(0, numColsProductMatrix):
			element = productFormula(i, j, matrix1, matrix2, findNumCols(matrix1))
			productMatrix[i].append(element)
	return productMatrix

def productFormula(i, j, A, B, m):
	outputNumber = 0
	for k in range(0, m):
		outputNumber = outputNumber + f(i, j, A, B, k)
	return outputNumber

def f(i, j, A, B, k):
	return A[i][k] * B[k][j]	


firstMatrix = askUserMatrix()
secondMatrix = askUserMatrix()


productM = productMatrix(firstMatrix, secondMatrix)
print firstMatrix
print secondMatrix
print productM
