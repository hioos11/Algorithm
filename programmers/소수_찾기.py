import math
from itertools import permutations

# 소수인지 판단하는 함수
def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False

        return True
    
def solution(numbers):
    answer = []
    
    for i in range(1, len(numbers)+1):
        # 1 ~ len(numbers)개의 순열 리스트 생성
        arr = list(permutations(numbers, i))
        
        # 리스트의 튜플을 숫자로 바꿔 소수인지 판단
        for j in range(len(arr)):
            num = int(''.join(map(str,arr[j])))
            if isPrime(num):                
                answer.append(num)
    # 중복 제거
    answer = set(answer)
    return len(answer)