from collections import deque

def bfs_by_queue(root):
  queue = deque([root])
  while len(queue) > 0:
    node = queue.popleft()
    for child in node.children:
      if child:
        return child
      queue.append(child)
  return 'NOT_FOUND'
        
  