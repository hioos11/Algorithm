
'''
2번문제
def solution(s):
    answer = -1
    idx = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            idx += 1
        else: 
            idx = 0
        
        if idx == 2:
            answer = max(int(s[i-1: i+2]), answer)
            
    return answer

#print(solution("123"))
'''

# 3번문제
def solution(amountText):
    answer = True
    for i in range(len(amountText)):
        a = amountText[i]
        if i == 0 and a == '0':
            return False
        
        if a.isdigit() == False and a != ',':
            return False
        
        if a == ',':
            if (len(amountText) - i ) % 4 != 0:
                return False

    if amountText[0] == ',' or amountText[len(amountText)-1] == ',':
        return False

    return answer

#print(solution("10000")) # true
#print(solution("25,000")) # true
#print(solution("39,00")) # false
print(solution("0100")) # false
