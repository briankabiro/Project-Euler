total = 0
odd = [x for x in range(2,2000000) if x % 2 != 0]
n = len(odd) - 1
n = odd[n]
multiples = set()
for i in range(2,n+1):
	if i not in multiples:
		total += i
		multiples.update(range(i * i, n+1,i))
print(total)
##142913828924