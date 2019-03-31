def swap_case(s):
  res=""
  for i in range(len(s)):
    if 65<=ord(s[i])<=90:
      res+=chr(ord(s[i])+32)
    elif 97<=ord(s[i])<=122:
      res+=chr(ord(s[i])-32)
    else:
      res+=s[i]
  return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)