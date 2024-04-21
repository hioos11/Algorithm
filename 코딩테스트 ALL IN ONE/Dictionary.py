'''
문제에서 언제 써야 하는지 어떤 연산을 해야하는지 알아두는 것이 중요.

'''

listScore = [97, 49, 89] # 어떤 점수가 어떤 과목의 점수인지 알 수 없다. -> Dictionary 사용
dicScore = {
    'math' : 97,
    'eng' : 49,
    'kor' : 89
} # 키 값은 중복되면 안됨

print(dicScore['math'])

dicScore['math'] = 45 # 기존 score수정
dicScore['sci'] = 100 # 기존에 존재하지 않던 새로운 key-value 추가
print(dicScore['sci'])

