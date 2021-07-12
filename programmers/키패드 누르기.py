def solution(numbers, hand):
    answer = ''
    numpad = {1:[0,0], 2:[1,0], 3:[2,0], 4:[0,1], 5:[1,1], 6:[2,1], 7:[0,2], 8:[1,2], 9:[2,2], '*':[0,3], 0:[1,3], '#':[2,3] }
    left = numpad['*']
    right = numpad['#']
    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            left = numpad[n]
        elif n in [3, 6, 9]:
            answer += 'R'
            right = numpad[n]
        else:
            leftD = 0
            rightD = 0
            # left, right, numpad는 좌표 형태이기 때문에 x와 y좌표를 각각 거리 계산해야함
            for a, b, c in zip(left, right, numpad[n]):
                leftD += abs(a-c)
                rightD += abs(b-c)
            if leftD < rightD:
                answer += 'L'
                left = numpad[n]    
            elif leftD > rightD:
                answer += 'R'
                right = numpad[n]
            else:
                if hand == 'left':
                    answer += 'L'
                    left = numpad[n]
                else:
                    answer += 'R'
                    right = numpad[n]
    return answer
  
  # zip 함수
  # 딕셔너리를 좌표 형태로 저장해서 쌍으로 계산하기
