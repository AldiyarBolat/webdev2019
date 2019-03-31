import math
x = int(input())

i = 2
while i < x + 1:
	if x % i == 0:
		print(i)
		break
	i+=1