import heapq

def solution(jobs):
    answer = 0
    count = 0
    last = -1
    heap = []
    jobs.sort()
    time = jobs[0][0]
    while count < len(jobs):
        for s, t in jobs:
            if last < s <= time:
                # 시간으로 정렬되어야 하기 때문에 t,s로 들어감
                heapq.heappush(heap, (t,s))
        if len(heap) > 0:
            count += 1
            last = time
            term, start = heapq.heappop(heap)
            time += term
            answer += (time - start)
        else:
            time += 1
        
    return answer // len(jobs)
