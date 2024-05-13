'''
레벨오더 순회방식으로 풀기
레벨오더 -> bfs와 거의 동일한 방식 => queue로 진행

레벨오더 순회를 구현하기 위해서는
1. 큐 선언
2. 첫번째 방문할 노드를 인큐
3. 와일문으로 큐가 비어있을 때까지 계속 반복
4. 와일문 안에서 방문하고 dequeue(popleft)
5. 현재 노드의 자식 노드들을 모두 enqueue
6. max depth 최신화 

결국 노드의 개수만큼 코드를 실행하므로 시간복잡도는 O(n)



'''
from collections import deque

# 기본 템플릿
def bfs(root):
    visited = []
    if root is None:
        return 0
    q = dequeue()
    q.append(root)
    while q:
        cur_node = q.popleft()
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)

    return visited

#bfs(root)

# lever order 방식
def maxDepth(root):
    # visited 대신에 depth를 처리하는 방식
    max_depth = 0

    if root is None:
        return max_depth
    
    q = deque()
    q.append((root, 1))
    while q:
        cur_node, cur_depth = q.popleft()
        
        max_depth = max(max_depth, cur_depth)

        if cur_node.left:
            q.append((cur_node.left, cur_depth+1))
        if cur_node.right:
            q.append((cur_node.right, cur_depth+1))

    return max_depth

root = [3,9,20,None,None,15,7]

class TreeNode:
    def __init__(self, l=None, r=None, v=0):
        self.left = l
        self.right = r
        self.value = v

# root = TreeNode(v = 3)
# root.left = TreeNode(v=0)
# root.right = TreeNode(v=20)
# root.right.left = TreeNode(v=15)
# root.right.right = TreeNode(v=7)

#print(maxDepth(root))


# post order 방식
'''
모든 childnode를 방문하고 그 이후에 나 자신을 방문하는게 post order

'''

def maxDepthPostOrder(root):
    if root is None:
        return 0
    left_depth = maxDepthPostOrder(root.left)
    right_depth = maxDepthPostOrder(root.right)
    return max(left_depth, right_depth) + 1



root = TreeNode(v = 3)
root.left = TreeNode(v=0)
root.right = TreeNode(v=20)
root.right.left = TreeNode(v=15)
root.right.right = TreeNode(v=7)
print(maxDepthPostOrder(root))