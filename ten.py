total = 2
not_prime = []
odd = [x for x in range(2,2000000) if x % 2 != 0]
n = len(odd) - 1
n = odd[n]

def rwh_primes(n):
	sieve = [True] * n
	for i in range(3,int(n**0.5)+1,2):
		if sieve[i]:
			sieve[i*i::2*i] = [False] * ((n-i*i-1)/(2*i)+1)
	return [2] + [i for i in range(3,n,2) if sieve[i]]
rwh_primes(n)