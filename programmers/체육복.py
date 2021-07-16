# 리스트는 차집합 연산이 불가능 하지만 set은 차집합 연산 가능
def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    total = []
    for i in range(1, n+1):
        if i not in set_lost:
            total.append(i)
            
    for r in set_reserve:
        if r-1 in set_lost:
            total.append(r-1)
            set_lost.remove(r-1)
            continue
        elif r+1 in set_lost:
            total.append(r+1)
            set_lost.remove(r+1)
            continue
    return len(total)

# 좀 더 간단한 코드
def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)

    for r in set_reserve:
        if r-1 in set_lost:
            set_lost.remove(r-1)
        elif r+1 in set_lost:
            set_lost.remove(r+1)
    return n - len(set_lost) 

# 나는 따로 total이라는 리스트를 만들어 최종적으로 체육 시간에 참가 가능한 번호를 추가했지만, 최종적으로 set_lost에 남은 요소 개수를 총 개수에서 빼면 간단히 리턴 가능.