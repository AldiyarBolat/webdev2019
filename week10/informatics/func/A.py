def mini(a, b, c, d):
    return  min(a, b, c, d)
array = list(map(int, input().split()))
print(mini(array[0], array[1], array[2], array[3]))