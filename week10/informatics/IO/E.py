v = int(input())
t = int(input())

if v>0:
  res = (v*t)%109
elif v<0:
  res = 109 - ((-1*v*t)%109)
else:
  res = 0
       


if res==109:
  res=0
       

print(res)