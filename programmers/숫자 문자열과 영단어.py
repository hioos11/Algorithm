def solution(s):
    number = {'zero':'0', 'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    temp = ''
    answer = ''
    for c in s:
        if c in '0123456789':
            answer += c
        else:
            temp += c
        
        if temp in number.keys():
            answer += number[temp]
            temp = ''
    return int(answer)
