total = 0
for i in range(2,1000000):
	for x in range(2,(i-1)):
		if(i % x) == 0:
			break
	else:
		total +=1
		if(total == 10001):
			print("this is the prime",i)
			break