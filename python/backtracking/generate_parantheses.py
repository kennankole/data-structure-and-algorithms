from typing import List
def generate_parantheses(n: int) -> List[str]:
  '''
  1. Only add open parantheses when open < n
  2. Only add a closing paranthese when close < open
  3. The code is valid if and only if open == closed == n
  '''
  stack = []
  ans = []
  
  def backtracking(openBracket, closeBracket):
    if openBracket == closeBracket == n:
      ans.append("".join(stack))
      return
    
    if openBracket < n:
      stack.append("(")
      backtracking(openBracket + 1, closeBracket)
      stack.pop()
      
    if closeBracket < openBracket:
      stack.append(")")
      backtracking(openBracket, closeBracket + 1)
      stack.pop()

  backtracking(0, 0)
  return ans


# Using dfs
def generate_paranthese_combination(n):
  def dfs(start_index, path, open_count, close_count, res):
    if start_index == 2 * n:
      res.append(''.join(path))
      return
    if open_count < n:
      path.append('(')
      dfs(start_index + 1, path, open_count + 1, close_count, res)
      path.pop()
    if close_count < open_count:
      path.append(')')
      dfs(start_index + 1, path, open_count, close_count + 1, res)
      path.pop()
  ans = []
  dfs(0, [], 0, 0, ans)
  return ans

print(generate_paranthese_combination(3))