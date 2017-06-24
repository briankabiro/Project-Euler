##start from half, if i find a number run function to check if it is a prime number
primes = []
square_root = int(600851475143 ** 0.5)

def getAllPrimes():
	for i in range(square_root,2,-1):
		for x in range((i-1),2,-1):
			if(i % x) == 0:
				break
		else:
			if(600851475143 % i == 0):
				print("this is the prime",i)
				return True
getAllPrimes()
