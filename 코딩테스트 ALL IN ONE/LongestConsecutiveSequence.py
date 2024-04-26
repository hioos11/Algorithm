'''

'''

def longestConsecutive(nums):
    logest = 0
    num_dict = {}
    for num in nums:
        num_dict[num] = True
    # 여기까지가 O(n)

    for num in num_dict: # for문의 in과 아래 if문에서의 in은 다르다. for문은 list를 iterate하게 접근한다는 의미
        if num - 1 not in num_dict: 
            # 이 조건문이 존재하기에 시간초과가 나지 않는다. 
            # 이 조건문이 없었더라면 아래의 while문이 N번 반복되어 시간복잡도가 N2(n제곱)이 됐을 텐데 
            # 이 조건문 덕분에 O(n)이 될 수 있다.
            cnt = 1
            target = num + 1
            while target in num_dict:
                target += 1
                cnt += 1
            longest = max(longest, cnt)
    # 여기까지도 O(n)
    return longest

longestConsecutive([6, 7, 100, 5, 4, 4])

# in 연산을 사용하기 위해 딕셔너리를 사용했는데 key-value 로 데이터가 존재하기 때문에 불필요한 value 들을 넣어줬다.
# 해시셋을 사용하면 불필요한 value를 사용하지 않아도 된다.
