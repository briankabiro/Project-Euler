numbers = [1,2]

def getAllPrimes():
	number = numbers[len(numbers) - 1] + numbers[len(numbers) - 2]
	if number < 4000000:
		numbers.append(number)
		getAllPrimes()
	else:
		addToArray()

def addToArray():
	total = 0
	for number in numbers:
		if (number % 2 == 0):
			total = total + number
	print("this is the total", total)

getAllPrimes()
