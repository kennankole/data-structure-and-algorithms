#Without memoization
def word_break(target, words):
  def dfs(start_index):
    if start_index == len(target):
      # print(start_index)
      return True
    answer = False
    for word in words:
      if target[start_index:].startswith(word):
        answer = answer or dfs(start_index + len(word))
      print(word)
    return answer
  return dfs(0)


#With memoization
def word_break_memoization(words, target):
  memo = {}
  def dfs(start_index):
    if start_index == len(target):
      return True
  
    if start_index in memo:
      return memo[start_index]
    
    answer = False
    for word in words:
      if target[start_index:].startswith(word):
        if dfs(start_index + len(word)):
          answer = True
          break
    
    memo[start_index] = answer
    return answer
  return dfs(0)
  
target = "algomonster"
words = ["algo", "monster"]
print(word_break_memoization(target=target, words=words))