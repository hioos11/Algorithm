'''
딕셔너리를 사용할 때 기억하고싶은 값이 있다면 그 값은 key에 저장해야 한다. (value가 아니라)

이 문제의 경우 value에는 별다른 값을 넣어주지 않아도 된다. 적당히 그냥 True나 아무 문자열이여도 좋다. 어차피 key값만 볼거기 때문에

'''

def two_sum(nums, target):
    memo = {}   # 딕셔너리 선언
    for v in nums:
        memo[v] = 1

    for v in nums:
        num = target - v
        if v == num:
            continue
        if num in memo: # list인 nums가 아니라 딕셔너리인 memo에서 찾아야한다는 것에 유의하기
            return True
        
    return False