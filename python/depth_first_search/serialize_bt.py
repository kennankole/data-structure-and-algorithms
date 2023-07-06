from node import Node

def serialize(root: Node):
  results = []
  def dfs(root):
    if not root:
      results.append('X')
      return
    results.append(root.val)
    results.append(root.left)
    results.append(root.right)
  dfs(root)
  return ' '.join(results)
