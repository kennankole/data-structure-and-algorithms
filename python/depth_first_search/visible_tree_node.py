from node import Node

def visible_tree_node(root: Node):
  def dfs(root, max_value_so_far):
    if not root:
      return 0
    total = 0
    if root.val >= max_value_so_far:
      total += 1
    total += dfs(root.left, max(max_value_so_far, root.val))
    total += dfs(root.right, max(max_value_so_far, root.val))
    return total
  return dfs(root, -float('inf'))
