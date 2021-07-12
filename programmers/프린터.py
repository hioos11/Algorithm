# 내 코드
# location이 맨 뒤로 갈때 처리 해주기
def solution(priorities, location):
    answer = 0
    
    while priorities:
        p = priorities.pop(0)
        location -= 1
        flag = 0
        for tmp in priorities:
            if p < tmp:
                priorities.append(p)
                if location == -1:
                    location = len(priorities)-1
                flag = 1
                break
        if flag == 0:
            answer += 1
            if location == -1:
                return answer
    
    return answer
  

# 더 간단한 코드
# pop 위치 유의하기
def solution(priorities, location):
    answer = 0
    queue = [(i,p) for i, p in enumerate(priorities)]
    
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
