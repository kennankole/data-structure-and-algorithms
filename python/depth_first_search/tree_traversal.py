class Node:
  def __init__(self, val, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right
    
def inorder_traversal(root: Node):
  '''
  left
  node
  right
  '''
  if root is not None:
    inorder_traversal(root.left)
    print(root.val)
    inorder_traversal(root.right)
    
  return

def pre_order_traversal(root: Node):
  '''
  node
  left
  right
  '''
  if root is not None:
    print(root.val)
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)
  return

def post_order_traversal(root: Node):
  '''
  left
  right
  node
  '''
  if root is not None:
    post_order_traversal(root.left)
    post_order_traversal(root.right)
    print(root.val)
  return
