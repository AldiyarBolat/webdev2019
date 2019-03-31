def lone_sum(a, b, c):
  if a != b and b != c and a!=c:
    return a + b + c
  elif a == b and b == c:
    return 0
  elif a == b and b!=c:
    return c
  elif a == c and a!= b:
    return b
  else:
    return a
