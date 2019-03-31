import math
x = int(input())
i = 0

while math.pow(2, i)<=x:
	a = (math.pow(2, i))
	print(int(math.floor(a)))
	i+=1
