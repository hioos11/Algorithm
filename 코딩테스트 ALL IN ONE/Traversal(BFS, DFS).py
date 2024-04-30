'''
트리 순회(Tree Traversal)
트리 탐색(search)라고도 불리며 트리의 각 노드를 방문하는 과정을 말한다. 모든 노드를 한 번씩 방문해야 하므로 완전 탐색이라고도 불린다.
순회 방법으로는 너비 우선 탐색(BFS)과 깊이 우선 탐색(DFS)가 있다.

너비 우선 탐색(BFS)
루트 노드를 기준으로 루트 노드에서 가까운 노드부터 탐색하고 그 다음 레벨의 가까운 노드를 탐색하는,
레벨 순서대로 탐색하는 기법.
'''

# 템플릿처럼 외우기. 안보고도 짤 수 있게
def bfs(root):
    visited = []
    if root is None:
        return visited # 빈 리스트 리턴
    q = deque()
    q.append(root)
    # 여기까지가 초기 세팅


    # q가 빌 때까지 반복문 실행하면 모든 노드를 방문해 bfs완료
    while q:
        cur_node = q.popleft() # 접근과 방문은 다른데, cur_node를 통해 접근. 방문은 일단 접근을 해서 무언가 행위를 하는 것. popleft가 dequeue
        visited.append(cur_node.value) # 방문했다고 visited에 표시

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited


'''
깊이 우선 탐색(DFS)

DFS를 구현하는 방법은 두 가지가 있는데
1. stack을 이용해 반복문으로 구현
2. 재귀를 이용해서 구현

'''
# 재귀로 구현한 DFS
def dfs(cur_node):
    if cur_node is None:
        return
    
    dfs(cur_node.left)
    dfs(cur_node.right)