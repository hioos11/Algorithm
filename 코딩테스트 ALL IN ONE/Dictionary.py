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

dicScore['math'] = 45 # 기존 score수정(97 -> 45)
dicScore['sci'] = 100 # 기존에 존재하지 않던 새로운 key-value 추가
print(dicScore['sci'])

#print(dicScore['music'])  # 에러남. 존재하지 않는 키이기 때문에.

print('music' in dicScore) # False

if 'music' in dicScore:   ## key in dictionary : key를 가지고 있는지 없는지를 시간복잡도 O(1)으로 바로 알 수 있다.
    print(dicScore['music'])
else:
    dicScore['music'] = 0

'''
리스트로 관리하는 어떤 데이터에 특정 값이 존재하는지 여부를 판단하기 위해서는
리스트의 경우, 하나하나 접근해서 알아가야 하는데 데이터가 굉장히 많은 경우 시간복잡도도 커진다.
하지만 딕셔너리의 경우 in 으로 key의 존재 여부를 O(1)로 판단할 수 있다.
딕셔너리는 시간복잡돌르 줄이기 위해서 메모리를 사용하는 것이다.

딕셔너리는 코테 문제에도 많이 나오고 쓸 수 있는 상황을 판별하는 것이 굉장히 중요하다.
'''