# 입력받은 문자열을 모두 대문자로 변경
s = input().upper()

# 딕셔너리 선언
d = dict()

for i in s:
  # 해당 문자가 딕셔너리에 없는 경우에
  if i not in d:
    # 문자열에서 해당 문자 개수를 딕셔너리에 저장
    # key : 문자, value : 문자열에서 문자 개수
    d[i] = s.count(i)
    
# 딕셔너리의 value들을 리스트로 변경 후 최대값을 가진 key의 개수가 2이상인 경우
if (list(d.values())).count(max(d.values())) > 1:
  print('?')
# 유일한 최대값을 가진 경우
else:
  # 딕셔너리의 key와 value에 items()로 접근
  for key, val in d.items():
    # val이 최대값인 경우 key 출력
    if val == max(d.values()):
      print(key)
      
# dictionary 사용법 알기
