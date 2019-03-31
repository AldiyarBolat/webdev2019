names = []
scores = []
n = int(input())

for i in range(0, n):
    name = input()
    score = float(input())
    names.append(name)
    scores.append(scores)

    mini = min(scores)
    maxi = max(scores)

for i in range(0, n):
    if scores[i] != mini:
        if maxi > scores[i]:
            maxi = scores[i]

lis = []
for i in range(0, n):
    if(scores[i] == maxi):
        lis.append(names[i])
for i in range(len(lis)):
    print(lis[i])
