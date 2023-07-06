from node import Node

#https://leetcode.com/problems/maximum-depth-of-binary-tree/
def max_depth(root: Node) -> int:
  '''
  Max depth of a binary tree is the longest root-to-leaf path.
  '''
  if root is None:
    return 0
  left = max_depth(root.left)
  right = max_depth(root.right)
  return 1 + max(left, right)

def tree_max_depth(root: Node):
  def dfs(root):
    if not root:
      return 0
    # num nodes in longest path of current subtree = max num nodes of its two subtrees + 1 current node
    return max(dfs(root.left), dfs(root.right)) + 1
  return dfs(root) - 1 if root else 0
