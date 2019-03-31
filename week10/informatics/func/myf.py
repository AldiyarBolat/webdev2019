def And(a, b):
	return  a and b



array = list(map(int, input().split()))
print(And(array[0], int(array[1])))