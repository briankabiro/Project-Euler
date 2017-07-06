largest = 0
number = 0
for i in range(1,1000000):
	print(i)
	n = i
	count = 0
	while i >= 1:
		if i == 1:
			break
			count = count + 1
		if (i % 2 == 0):
			i = i/2
			count = count + 1
		else:
			i = 3*i + 1
			count = count + 1
	if count > largest:
		largest = count
		number = n
print("this is the number and the number of steps",number,largest)
#837799 524
		