def all_permutations(letters):
  def dfs(start_index, path, used):
    if start_index == len(letters):
      res.append(''.join(path))
    
    for i, letter in enumerate(letters):
      if used[i]:
        continue
      path.append(letter)
      used[i] = True
      dfs(start_index + 1, path, used)
      path.pop()
      used[i] = False
  res = []
  dfs(0, [], [False] * len(letters))
  return res

print(all_permutations("ABC"))