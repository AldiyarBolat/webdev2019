import math

a = int(input())
cnt = 0

for i in range(1, a + 1):
	if a % i == 0:
		cnt++


print(cnt)		
		
