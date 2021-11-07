def totalValue(Num):
	Num1 = 0
	val = 1
	for _ in range(0, Num):
		Num1 += val
		val += 2
	return len(str(Num1))


n = 25
num = 1
space = ""
spaceN = totalValue(n)
for i in range(spaceN + 1):
	space += " "
for i in range(n + 1):
	for j in range(0, n - i):
		print(space, sep="", end="")
	for k in range(0, i):
		numSpace = space[len(str(num)):]
		print(num, numSpace, sep="", end="")
		num += 1
	for j in range(0, i - 1):
		numSpace = space[len(str(num)):]
		print(num, numSpace, sep="", end="")
		num += 1
	print()