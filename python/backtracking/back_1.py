from typing import List
'''
Backtracking problem solution template
function dfs(start_index, path):
  if is_leaf(start_index):
    report(path)
    return
  for edge in get_edges(start_index):
    path.add(edge)
    dfs(start_index + 1, path)
    path.pop()
'''
def letter_combination(n: int) -> List[str]:
  def dfs(start_index, path):
    if start_index == n:
      res.append(''.join(path))
      return
    for letter in ["a", "b"]:
      path.append(letter)
      dfs(start_index+1, path)
      path.pop()
  res = []
  dfs(0, [])
  return res
