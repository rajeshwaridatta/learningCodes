from mathutil import arsinh
'''def askUser():
	return float(raw_input('Enter the number: '))

x = askUser()
print "arsinh(" + str(x) + ") = " + str(arsinh(x))
'''
 
def evenOrOdd():
	while True:
		try:
			n = int(raw_input('Enter the number: '))
			break
		except ValueError:
			print "Please provide an integer number"

	if n%2==0:
		print str(n) +" " + "is an even number"
	else:
		print str(n) +" " + "is an odd number"

evenOrOdd()
