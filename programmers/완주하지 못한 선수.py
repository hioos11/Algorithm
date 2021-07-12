# 정확성 테스트는 통과하지만 효율성 테스트는 실패
def solution(participant, completion):
    answer = ''
    for c in completion:
        if c in participant:
            participant.remove(c)

    answer = ''.join(participant)
    
    return answer
  
# 효율성 테스트 통과하는 답안(구글링)
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for a, b in zip(participant, completion):
        if a != b:
            return a
    
    return participant.pop()
  
# 효율성 통과하기 위해 collections를 많이 사용.
# collections
