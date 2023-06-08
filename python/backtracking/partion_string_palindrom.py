from typing import List

def partion(s: str) -> List[List[str]]:
  ans = []
  n = len(s)
  
  def is_palindrome(word):
    return word == word[::-1]
  
  def dfs(start, curr_path):
    if start == n:
      ans.append(curr_path[:])
      return
    for char in range(start + 1, n + 1):
      prefix = s[start:char]
      if is_palindrome(prefix):
        dfs(char, curr_path + [prefix])
  dfs(0, [])
  return ans


print(partion("aab"))