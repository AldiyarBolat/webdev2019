import math
a = int(input())
array = list(map(int, input().split()))

for i in range(0, a):
	if i % 2 == 0:
		print(array[i])