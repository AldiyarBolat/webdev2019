import math
a = int(input())
array = list(map(int, input().split()))
ok = False

for i in range(1, a):
	if (array[i] > 0 and array[i - 1] > 0) or (array[i] < 0 and array[i - 1] < 0) :
		ok = True
		break

if ok:
	print("YES")
else:
	print("NO")	
