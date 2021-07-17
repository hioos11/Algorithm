# 마지막 테스트 케이스 통과 못하는 버전
def solution(name):
    moves = [min(ord(s) - ord('A'), ord('Z') - ord(s) + 1) for s in name]
    
    answer = 0
    
    index = 0
    while True:
        
        answer += moves[index]
        moves[index] = 0
        
        if sum(moves) == 0:
            return answer
        

        left, right = 0, 0

        while True:
            right += 1
            if moves[index + right] != 0:
                break
        while True:
            left += 1
            if moves[index - left] != 0:
                break
        
        if left < right:
            index -= left
            answer += left

        else:
            index -= right
            answer += right
            
# 테스트 케이스 통과 버전
def solution(name):
    moves = [min(ord(s) - ord('A'), ord('Z') - ord(s) + 1) for s in name]
    
    answer = 0
    
    index = 0
    
    while True:
        
        answer += moves[index]
        moves[index] = 0
        
        if sum(moves) == 0:
            return answer

        left, right = 0, 0

        while True:
            right += 1
            if moves[index + right] != 0:
                break
        while True:
            left += 1
            if moves[index - left] != 0:
                break
        
        # 이 부분만 다르다
        # 뭐가 다른지는 아직 모르겠다
        answer += left if left < right else right
        index += -left if left < right else right


###########
        left, right = 0, 0

        while True:
            right += 1
            if moves[index + right] != 0:
                break
        while True:
            left += 1
            if moves[index - left] != 0:
                break

# 이 부분을 
        left, right = 1, 1

        while moves[index + right] == 0:
            right += 1
        while moves[index - left] == 0:
            left += 1
# 이렇게도 표현 가능