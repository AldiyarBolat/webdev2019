import math

a = int(input())
b = int(input())

for i in  range(a, b):
	c = math.sqrt(i)
	if math.ceil(c) == math.floor(c):
		print(i)

