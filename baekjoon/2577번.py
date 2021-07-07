temp = 1
for _ in range(3):
  temp *= int(input())
temp = str(temp)
for i in range(10):
  print(temp.count(str(i)))
