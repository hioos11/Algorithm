def solution(brown, yellow):
    answer = []
    
    total = brown + yellow
    
    for i in range(2, total):
        if total % i == 0:
            y = i
            x = total // y
            if (x-2) * (y-2) == yellow:
                answer.append(x)
                answer.append(y)
                return answer