## get triangle number, get divisors, check if less than 500, add one
n = 1
divisors = 1
number = 0
while divisors < 500:
	divisors = 1
	number = n
	triangleNumber = ((n + 1) *  n)/2
	for x in range(1,n+1):
		if triangleNumber % x == 0:
			divisors = divisors + 1
	n = n + 1
print("this is the number and its divisors",number,triangleNumber,divisors)
##41041 550