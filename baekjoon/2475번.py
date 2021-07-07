data = list(map(int, input().split()))
temp = 0
for d in data:
  temp += d * d
print(temp%10)
