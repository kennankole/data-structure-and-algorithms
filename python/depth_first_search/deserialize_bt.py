from node import Node

def serialize(s):
  def dfs(root):
    value = next(root)
    if value == 'x': return
    current_node = Node(int(root))
    current_node.left = dfs(root)
    current_node.right = dfs(root)
    return current_node
  return dfs(iter(s.split()))
  