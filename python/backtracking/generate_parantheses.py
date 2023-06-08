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

print(generate_parantheses(3))