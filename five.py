##get smallest natural number divisible by 1..20
def checkIfDivisible():
	for i in range(2,21):
		for x in range(2,(i-1)):
			if (i % x) == 0:
				break
			else:
				print("this be a prime", i)

checkIfDivisible()