##start from half, if i find a number run function to check if it is a prime number
primes = []
square_root = int(600851475143 ** 0.5)

def getAllPrimes():
	for i in range(2,square_root):
		for x in range(2,(i-1)):
			if(i % x) == 0:
				break
		else:
			if(600851475143 % i == 0):
				print("I found a prime",i)
				primes.append(i)
getAllPrimes()
