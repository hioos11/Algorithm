def solution(array, commands):
    answer = []
    for com in commands:
        a, b, c = com
        temp = array[a-1:b]
        temp.sort()
        answer.append(temp[c-1])
    return answer
