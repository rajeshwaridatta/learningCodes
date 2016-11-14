import math
def inputPower():
	a= float(raw_input("Enter the First number: "))
	b= float(raw_input("Enter the second number: "))
      
	p=math.pow(a,b)
	print str(a)+"^"+str(b)+"="+ str(p)
inputPower()
