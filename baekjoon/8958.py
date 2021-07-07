# 테스트 케이스 개수
N = int(input())
# 각 테스트 케이스의 점수를 저장할 리스트
score = []

for _ in range(N):
  # 테스트 케이스 입력
  t = input()
  # 현재 t의 점수를 저장할 변수
  num = 0
  # 연속된 정답인 경우를 판단할 수 있는 변수
  # 연속된 정답인 경우 temp가 2, 3 ...으로 증가
  temp = 0
  for i in range(len(t)):
    if t[i] == 'O':
      temp += 1
      # 증가된 temp를 num에 더함
      num += temp 
    else:
      # 틀렸을 경우 temp를 0으로 초기화
      temp = 0
  score.append(num)
for i in score:
  print(i)
