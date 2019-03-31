def mini(a, b):
	return  a**b
array = list(map(float, input().split()))
print(mini(array[0], int(array[1])))