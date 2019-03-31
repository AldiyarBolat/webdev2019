import math
a = int(input())
array = list(map(int, input().split()))

for i in range(0, a):
	if array[i] % 2 == 0:
		print(array[i])