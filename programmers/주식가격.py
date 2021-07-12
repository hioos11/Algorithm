def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for t, p in enumerate(prices):
        
        while stack and stack[-1][1] > p:
            a, b = stack.pop()
            answer[a] = t - a
        else:
            stack.append([t, p])
        
    while stack:
        a, b = stack.pop()
        answer[a] = len(prices) - 1 - a
    
    
    return answer
