abundantNumbers = set()
for i in range(1,28131):
	sumOfdivisors = 0
	sqrRoot = int(i**0.5)
	for x in range(1,sqrRoot+1):
		if i % x == 0:
			sumOfdivisors += x
			if i/x != x and i/x != i:
				sumOfdivisors += i/x
	if(sumOfdivisors > i):
		abundantNumbers.add(i)
print(len(abundantNumbers))

expressedNumbers = set()
for i in abundantNumbers:
	for x in abundantNumbers:
		integer = i + x
		if(integer < 28123):
			if integer not in expressedNumbers:
				expressedNumbers.add(integer)

if 24 in expressedNumbers:
	print("24 checks out")
if 30 in expressedNumbers:
	print("30 checks out")
naturalNumbers = set(range(28130))

nullNumbers = naturalNumbers - expressedNumbers
total = 0
for i in nullNumbers:
	total += i
print(total)
##4376753