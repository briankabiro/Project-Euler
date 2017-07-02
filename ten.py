total = 2
not_prime = []
odd = [x for x in range(2,2000000) if x % 2 != 0]
n = len(odd) - 1
n = odd[n]
for i in odd:
	if i not in not_prime:
		total += i
		if i > 1000000:
			print("we have hit a million")
		for j in range(i*i,n+1,i):
			not_prime.append(j)
print(total)