def askUserList():
	outputList = []
	n = int(raw_input("Enter the count of numbers: "))
	for i in range(0,n):
		num = float(raw_input("Enter the number[" + str(i+1) + "]: "))
		outputList.append(num)
	return outputList

#inputNumberList = askUserList()
#print inputNumberList

def sumOfDivisibles():
	totalsum=0
	n=int(raw_input("Enter the count of numbers: "))
	for i in range(0,n):
		number= int(raw_input("Enter the number[" + str(i+1) + "]: "))
		if number%3==0 or number%5==0:
			totalsum=totalsum+number
	print "total sum of numbers divisible by 3 or 5 is:"+ str(totalsum)
sumOfDivisibles()

				
