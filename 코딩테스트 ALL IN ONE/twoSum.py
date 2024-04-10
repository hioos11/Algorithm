# 완전탐색으로 풀기
def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return True
            
    return False

# 이 경우 시간복잡도가 O(n2)이 되기 때문에 문제 제한조건인 n4을 대입하면 시간복잡도가 n8까지 될 수 있기 때문에 시간 제한을 초과할 수 있다.
print(twoSum(nums = [4, 1, 9, 7, 5, 3, 16], target=14))


# 리스트를 정렬하는데 소요되는 시간복잡도는 O(nlogn)이다.
# 정렬 후 양 끝에서 하나씩 선택 후 더했을 때를 타겟과 비교 후 타겟보다 작으면 오른쪽 값을 한칸 왼쪽으로, 타겟보다 크면 왼쪽 값을 한칸 오른쪽으로 옮겨가며 비교한다.
# 같은 원소를 선택할 수 없기 때문에 왼쪽오른쪽 값이 같아지면 False 리턴한다.
# 이 로직은 처음에 리스트를 정렬하는데 소요되는 시간복잡도 O(nlogn)과 왼쪽 값(left)와 오른쪽 값(right)가 한칸 씩 옮겨가며 같은 값을 가리킬때가 가장 많이 실행되는 경우라 즉 O(n)의 시간복잡도를 가진다.
# 결국 전체적인 코드의 시간복잡도는 target을 찾는 시간복잡도보다 정렬하는데 시간복잡도가 더 크기 때문에 O(nlogn)이 전체 시간복잡도가 된다.

# 바로 코드를 짜면 안되고 코드 설계 후 코드를 구현해야 한다.

def twoSumByTwoPointer(nums, target):
    l = 0
    r = len(nums) -1

    nums.sort()

    while l < r :
        if nums[l] + nums[r] == target:
            return True
        elif nums[l]+nums[r] > target:
            r -= 1
        else:
            l += 1
    
    return False
print(twoSumByTwoPointer(nums = [4, 1, 9, 7, 5, 3, 16], target=14))

# 더 짧게 짠 코드
def twoSumByTwoPointerMoreSimple(nums, target):
    nums.sort()
    l, r = 0, len(nums)-1

    while l < r:
        if target > nums[l] + nums[r] : l += 1
        elif target < nums[l] + nums[r] : r -= 1
        else: return True