##check if a number is a palindrome -the last number should be equal to first number
def getPalindrome():
	largest = 0
	for i in range(999,100,-1):
		for x in range(999,100,-1):
			number = str(i * x)
			reversedNumber =  number[::-1]
			if int(reversedNumber) == int(number):
				if(int(number) > largest):
					largest = int(number)
	print(largest)
getPalindrome()