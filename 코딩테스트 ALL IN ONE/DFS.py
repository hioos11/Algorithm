'''
DFS는 방문 순서에 따라 종류가 세가지가 있다.
접근 순서는 모두 동일하다.

전위순회(preorder)
중위순회(inorder)
후위순회(postorder)
'''

# 전위순회
def preorder(cur_node):
    if cur_node is None:
        return
    
    print(cur_node.value) # 자손들에 접근하기 전에 먼저 방문.
    preorder(cur_node.left)
    preorder(cur_node.right)

preorder(root)

# 중위순회
def inorder(cur_node):
    if cur_node is None:
        return
    
    inorder(cur_node.left)
    print(cur_node.value)
    inorder(cur_node.right)

inorder(root)

# 후위 순회. 자식들에 모두 방문 후 자기 자신 방문
def postorder(cur_node):
    if cur_node is None:
        return
    
    postorder(cur_node.left)
    postorder(cur_node.right)
    print(cur_node.value)