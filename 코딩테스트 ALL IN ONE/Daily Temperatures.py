'''
Daily Temperatures
괄호 유효성 문제가 닫는 괄호가 나올때만 반응을 하는것 처럼 이문제 또한
더 높은 기온이 나올 때 반응을 한다.

이렇게 특정 조건이 될때 반응하는 문제들이 꽤 많다.

문제 제한조건을 따져보면 input의 제한 조건이 10의 5제곱까지기 때문에 시간복잡도  O(n2)로는 풀면 안된다. (10의 8제곱을 넘어가면 안되기 때문에)

따라서 전체 반복문을 한번만 도는 시간복잡도 O(n)으로 풀도록 접근해야 한다.
'''

def dailyTempleratures(temperatures):
    answer = [0] * len(temperatures)
    stack = []

    for cur_day, cur_temp in enumerate(temperatures):
        # 2차원 리스트에서 list[-1]이 의미하는건 마지막 로우를 의미하는건가
        # 생각해보니까 현재 선언된 stack은 2차원 리스트가 아니라 1차원인데 원소가 쌍으로 이루어진것.
        # 따라서 [-1]로 마지막 요소를 가져온다고 생각하면 될것같다. (pop으로 생각)
        # 그런데 아예 pop을 해버리면 stack 자체에서 삭제해 버리기 때문에 get의 용도로 [-1]를 사용한다고 생각하자.

        while stack and stack[-1][1] < cur_temp:
            prev_day, _ = stack.pop()
            answer[prev_day] = cur_day - prev_day

        stack.append((cur_day, cur_temp))
    return answer

print(dailyTempleratures([73,74,75,71,69,72,76,73]))