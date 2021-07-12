# 효율성 통과x
# 정확성도 일부 테스트케이스 통과x
# 66.7점
def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            isIn = phone_book[i].find(phone_book[j])
            if i != j and isIn != -1:
                answer = False
                
    return answer
  
# 효율성 일부 통과. 정확성도 일부 통과
# 75점
def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            isIn = phone_book[i].find(phone_book[j])
            if i != j and isIn != -1:
                return False
                
    return answer

# 구글링
def solution(phone_book):
    answer = True
    
    phone_book.sort()
    for a, b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            return False
    return answer
  
# startwsith 메소드 사용
