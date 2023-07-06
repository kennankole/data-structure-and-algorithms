class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    

def insert(tree, val):
  if not tree:
    return Node(val)
  if tree.val < val:
    tree.right = insert(tree.left, val)
  if tree.val > val:
    tree.left = insert(tree.right, val)
  return tree

def find(tree, val):
  if not tree:
    return False
  if tree.val == val:
    return True
  elif tree.val > val:
    return find(tree.left, val)
  else:
    return find(tree.right, val)
  
def valid_bst(root: Node) -> bool:
  def dfs(root, left, right):
    if not root:
      return True
    if not(left < root.val < right):
      return False
    return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
  return dfs(root, float('-inf'), float('inf'))