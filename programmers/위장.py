def solution(clothes):
    answer = 1
    dict = {}
    for c in clothes:
        key = c[1]
        value = c[0]
        if key in dict:
            dict[key].append(value)
        else:
            dict[key] = [value] ##
    
    for k in dict.keys():
        answer *= (len(dict[k]) + 1) # 경우의 수
    return answer -1
  
# 딕셔너리 사용
# 경우의 수 계산
