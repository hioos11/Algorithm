answer = [0  for _ in range(42)]
for _ in range(10):
  data = int(input())
  if answer[data%42] == 0:
    answer[data%42] += 1  
print(answer.count(1))
