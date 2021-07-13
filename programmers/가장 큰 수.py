def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    # 문자열 세번씩 반복해 아스키값으로 비교
    numbers.sort(key=lambda x:x*3, reverse = True)
    answer = str(int(''.join(numbers)))
    return answer
