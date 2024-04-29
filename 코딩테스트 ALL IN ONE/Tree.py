'''
Tree는 서로 연결된 Node의 계층형 자료구조로써, root와 부모-자식 관계의 subtree로 구성되어 있다.

Tree 관련 용어
- 노드(Node) : 트리는 보통 노드로 구현됨
- 간선(Edge) : 노드간에 연결된 선
- 루트 노드(Root) : 트리는 항상 루트에서 시작
- 리프 노드(Leaf) : 더이상 뻗어나갈 수 없는 마지막 노드
- 자식 노드(Child), 부모 노드(Parent), 형제 노드(Sibling)
- 차수(degree) : 각 노드가 갖는 자식의 수. 모든 노드의 차수가 n개 이하인 트리를 n진 트리라고 함
- 조상(ancestor) : 위쪽으로 간선을 따라가면 만나는 모든 노드
- 자손(descendant) : 아래쪽으로 간선을 따라가면 만나는 모든 노드
- 레벨(level) : 루트 노드에서 떨어진 거리
- 높이(height) : 루트노드에서 가장 멀리 있는 리프 노드까지의 거리. 즉, 리프 노드 중에 최대 레벨 값.
- 서브트리(subtree) : 트리의 어떤 노드를 루트로 하고, 그 자손으로 구성된 트리를 subtree라 한다.

이진트리(Binary Tree) 
- 모든 노드의 차수가 2개 이하인 트리
- 코딩테스트에 우선적으로 나오는 유형

완전 이진 트리(Complete Binary Tree)
- 이진 트리 중에서 마지막 레벨을 제외한 나머지 레벨에서 모든 노드가 채워져 있는 트리
- 마지막 레벨의 노드들은 왼쪽에서 오른쪽으로 순차적으로 채워진다.
- 힙 자료구조에서 중요하게 다뤄짐

Node
- 트리를 이루는 각 노드들은 value와 left child, right child의 주소를 각각 저장해야 한다.
'''

class Node : 
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left_child = left
        self.right_child = right

class BinaryTree:
    def __init__(self):
        self.root = None

bt = BinaryTree()
bt.root = Node(value=1)
bt.root.left = Node(value = 2)
bt.root.right = Node(value = 3)
bt.root.left.left = Node(value = 4)
bt.root.left.right = Node(value = 5) 
bt.root.right.right = Node(value = 6) 