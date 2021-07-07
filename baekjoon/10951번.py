import sys
for line in sys.stdin:
  a,b = map(int, line.split())
  print(a + b)

  
  ## 실패요인
  # input()과 stdin의 차이 알기
