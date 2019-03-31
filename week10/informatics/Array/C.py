import math
a = int(input())
array = list(map(int, input().split()))
cnt = 0

for i in range(0, a):
	if array[i] > 0:
		cnt += 1

print(cnt)
