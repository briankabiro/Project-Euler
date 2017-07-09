##1000 digit fibonacci number
fibonacciList = [1,1]
def fibonacci():
	length = len(fibonacciList)
	last = fibonacciList[length - 1]
	while len(list(str(last))) > 0:
		length = len(fibonacciList)
		last = fibonacciList[length - 1]
		secondlast = fibonacciList[length - 2]		
		number = last + secondlast
		fibonacciList.append(number)
		if len(list(str(last))) >= 1000:
			index = len(fibonacciList)
			print(index)
			break
	return index
print(fibonacci())
##4783