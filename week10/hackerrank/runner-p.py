x = int(input())

arr = list(map(int, input().split()))

m = max(arr)
mini = min(arr)

for i in range(0, x):
    if arr[i] != m:
        if mini < arr[i]:
            mini = arr[i]
print(mini)