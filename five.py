##get smallest natural number divisible by 1..20
##lcm(a,b,c) = lcm(a,lcm(b,c))
def gcd(a,b):
	while b:
		a,b = b, a % b
	return a

def lcm(a,b):
	return a * b // gcd(a,b)


def checkIfDivisible():
	number = 0
	for i in range(2,21):
		for x in range(2,i):
			if number == 0:
				number = (i * x)/gcd(i,x)
			else:
				number = (number * x)/gcd(number,x)
	print(number)


checkIfDivisible()
