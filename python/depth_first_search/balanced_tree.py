from node import Node

def is_balanced(root):
  if not root:
    return 0
  left = is_balanced(root.left)
  right = is_balanced(root.right)
  
  if left == - 1 or right == -1:
    return -1
  if abs(left - right) > 1:
    return -1
  return max(left, right) + 1

def valid_binary_tree(root: Node) -> bool:
  return is_balanced(root) != -1
