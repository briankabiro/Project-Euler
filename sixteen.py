total = 0
square = 2 ** 1000
while square:
	digit = square % 10
	total += digit

	square //= 10
print(total)