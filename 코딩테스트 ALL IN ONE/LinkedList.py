'''
linked list는 여러 개의 operation을 가지고 있다
get(), insert_back(), insert_front(), insert_at(), remove_back, remove_front(), remove_at() 등...

linked list는 물리적으로는 비연속적으로, 논리적으로는 연속적으로 저장되어 있다.

array는 메모리상에서도 연속적으로 저장되어있지만 linked list는 메모리상에서는 비연속적으로 저장되어 있다.
따라서 메모리적인 차이 때문에 시간복잡도가 다르다.

또한 linked lists는 메모리상에서 연속성을 유지하지 않아도 되기 때문에 메모리 사용이 자유롭다.
하지만 next node의 address를 추가적으로 저장해야 하기 때문에 데이터 하나당 차지하는 메모리는 더 커진다.

linked list는 코딩테스트에서 자주 나오는 유형은 아니지만 트리나 다른 자료구조를 구현할 때 linked list를 알아야 한다.
'''
class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third

# get()
# 특정 인덱스에 저장되어 있는 값을 가져온다.
# array라면 바로 원하는 인덱스에 접근이 가능하기 때문에 시간복잡도가 O(1)이겠지만 
# linked list는 무조건 head부터 시작해서 원하는 인덱스까지 이동해야 하기 때문에 O(n)의 시간복잡도를 가진다.

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None # 시간복잡도 O(1)의 append 구현할 때 사용

    def append1(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            # 맨 뒤의 node가 new_node를 가리켜야 한다.
            current = self.head
            while(current.next):
                current = current.next
            current.next= new_node

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

        new_node = Node(value)
        current = self.head

        for _ in range(idx-1):  # 직전 원소까지 이동해야 하니까 idx-1
            current = current.next
        
        # 기존 노드를 먼저 새로운 노드에 연결해야함
        new_node.next = current.next
        current.next = new_node

    def remove(self, idx):
        # 원하는 idx의 value 값 삭제
        current = self.head

        for _ in range(idx-1): # 얘도 직전 원소까지 이동해야 하니까 idx - 1
            current = current.next

        # current = idx - 1
        # current 가 idx의 다음을 가리켜야함
        current.next = current.next.next


    def append2(self, value):
        # insert_back
        # 시간복잡도 O(1)으로 구현하기
        # 마지막 노드를 가리키는 tail 사용해서 구현하기

        new_node = Node(value)
        if self.head is None:
            # 첫번째 노드가 들어올 때 head와 tail을 모두 설정해준다.
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

ll = LinkedList()

ll.append1(1)
ll.append1(2)
ll.append1(3)
ll.append1(5)
ll.append1(7)
ll.append1(8)
# 1, 2, 3, 5, 7, 8

ll.insert(3, 10)
# 1, 2, 3, 10, 5, 7, 8

ll.remove(1)
# 1, 3, 10, 5, 7, 8

print(ll.get(0))
print(ll.get(1))
print(ll.get(2))
print(ll.get(3))
print(ll.get(4))
print(ll.get(5))
