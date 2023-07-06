from node import Node

def invert_binary_tree_1(root):
  if not root:
    return
  return Node(root.value, invert_binary_tree_1(root.right), invert_binary_tree_1(root.left))


def invert_binary_tree2(root):
  if not root:
    return
  root.left, root.right = root.right, root.left
  invert_binary_tree2(root.left)
  invert_binary_tree2(root.right)
  return root