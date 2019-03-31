def xor(a, b):
	return  a^b
array = list(map(int, input().split()))
print(xor(array[0], int(array[1])))