def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    atmp, btmp, ctmp = 0, 0, 0
    
    for i in range(len(answers)):
        if a[i%len(a)] == answers[i]:
            atmp += 1
        if b[i%len(b)] == answers[i]:
            btmp += 1
        if c[i%len(c)] == answers[i]:
            ctmp += 1
    
    score_list = [atmp, btmp, ctmp]
    
    for person, score in enumerate(score_list):
        if score == max(score_list):
            answer.append(person+1)
    
    return answer