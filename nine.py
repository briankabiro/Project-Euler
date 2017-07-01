''' a squared + b squared < c a squared + b squared < c  '''
for i in range(1,700):
	for x in range(1,700):
		sum = i **2 + x **2
		sum = sum ** 0.5
		if int(sum) == sum:
			if (sum + i + x) == 1000:
				print(sum,i,x)
##200,375,425