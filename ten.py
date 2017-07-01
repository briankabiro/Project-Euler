total = 0
odd = [x for x in range(2,2000000) if x % 2 != 0]
for i in odd:
	for x in range(2,i-1):
		if (i % x) == 0:
			break
	else:
		total += i
print("this is the total",total)