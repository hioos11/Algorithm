'''
linked list는 여러 개의 operation을 가지고 있다
get(), insert_back(), insert_front(), insert_at(), remove_back, remove_front(), remove_at() 등...


'''

# get()
# 특정 인덱스에 저장되어 있는 값을 가져온다.
# array라면 바로 원하는 인덱스에 접근이 가능하기 때문에 시간복잡도가 O(1)이겠지만 
# linked list는 무조건 head부터 시작해서 원하는 인덱스까지 이동해야 하기 때문에 O(n)의 시간복잡도를 가진다.

class LinkedList(object):
    def __init__(self):
        self.head = None
    
    def append(self, value):
        pass

    def get(self, idx):
        # 1. head에 접근
        current = self.head

        # 2. 원하는 index로 이동
        for _ in range(idx):
            current = current.next  # 한 칸씩 이동

        # 3. value 반환
        return current.value
    
    def insert(self, idx, value):
        # append 코드 작업 후 직접 구현해보기
        # 원하는 idx에 value라는 값 삽입

    def remove(self, idx):
