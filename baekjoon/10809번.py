S = input()
data = [-1 for _ in range(26)]
word = 'a'
for i in range(26):
  if word in S:
    data[i] = S.index(word)
  word = chr(ord(word) + 1)
for i in range(26):
  print(data[i], end=' ')
  
# 아스키코드 값을 문자로 출력하는 메소드 chr
