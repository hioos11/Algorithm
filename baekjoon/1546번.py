N = int(input())
score = list(map(int, input().split()))
m = max(score)
for i in range(len(score)):
  score[i] = (score[i]/m) * 100

print(sum(score)/len(score))
