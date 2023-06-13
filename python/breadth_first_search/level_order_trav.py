from collections import deque
from typing import List

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val 
    self.left = left
    self.right = right 
  
def level_order_traversal(root: Node) -> List[List[int]]:
  res = []
  queue = deque([root])
  while len(queue) > 0:
    n = len(queue)
    new_val = []
    for _ in range(n):
      node = queue.popleft()
      new_val.append(node.val)
      for child in [node.left, node.right]:
        if child is not None:
          queue.append(child)
    res.append(new_val)
  return res