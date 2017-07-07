## get triangle number, get divisors, check if less than 500, add one
n = 1
divisors = 1
number = 0
while divisors < 500:
	divisors = 1
	number = n
	triangleNumber = ((n + 1) *  n)/2
	divisorsList = []
	squareRoot = int(triangleNumber ** 0.5)
	for x in range(1,squareRoot):
		if x in divisorsList:
			break
		if triangleNumber % x == 0:
			divisorsList.append(triangleNumber/x)
			divisors = divisors + 2
	print(number,triangleNumber,divisors)
	n = n + 1
print("this is the number and its divisors",number,triangleNumber,divisors)
##76576500
