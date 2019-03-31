x = int(input())

if x % 2 != 0:
    print('Weird')
elif x % 2 == 0 and (x > 1 and x < 6):
    print('Not Weird')
elif  x % 2 == 0 and (x > 5 and x < 21):
    print('Weird')
elif x % 2 == 0 and (x > 19):
    print('Not Weird')
