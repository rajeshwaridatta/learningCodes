import math

def sigmoid(x):
     a=math.e
     b=math.pow(a,-x)
     s= 1/(1+b)
     return s
def findQuadraticRoots(a,b,c):
	A= 2*a
	D= b*b-4*a*c
	if D<0:
		print "no real roots found"
		return
	if D==0:
		print -b/A
		return	
	B=math.sqrt(b*b-4*a*c)
	
	x1= (-b+B)/A
	x2= (-b-B)/A
	print x1,x2

def arsinh(x):
	a=math.sqrt(math.pow(x,2)+1)
	b= x+a
	y=math.log(b)
	return y	
