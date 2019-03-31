import math
a = int(input())
array = list(map(int, input().split()))
cnt = 0

for i in range(1, a - 1):
	if (array[i] > array[i - 1]) and (array[i] <  array[i - 1]) :
		cnt += 1


print(cnt)
