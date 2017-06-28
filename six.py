squares = [x ** 2 for x in range(101)]
totalSquares = 0

for square in squares:
	print(square)
	totalSquares += square

sumSquares = 0
for i in range(1,101):
	sumSquares += i

sumSquares = sumSquares ** 2

print(sumSquares- totalSquares)