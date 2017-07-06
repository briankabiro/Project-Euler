def factorial(n):
	if n == 1:
		return 1
	return n * (factorial(n-1))
answer = factorial(100)
answer = list(str(answer))
total = 0
for i in answer:
	total +=  int(i)
print(total)
##answer = 648