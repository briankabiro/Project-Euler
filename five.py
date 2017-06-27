##get smallest natural number divisible by 1..20
##lcm(a,b,c) = lcm(a,lcm(b,c))
def checkIfDivisible():
	for i in range(2,21):
		for x in range(2,i):
			if(i % x) == 0:
				break
			else:
				print("this is a prime",i)


checkIfDivisible()
def gcd(a,b):
	while b:
		a,b = b, a % b
	return a

def lcm(a,b):
	return a * b // gcd(a,b)
