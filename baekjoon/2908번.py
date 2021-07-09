def swap(s):
  s = "".join(reversed(s))
  return s
  
A, B = input().split()


A = int(swap(A))
B = int(swap(B))
if A > B:
  print(A)
else:
  print(B)

### join 용법 알기
### 문자열 뒤집기는 reversed
