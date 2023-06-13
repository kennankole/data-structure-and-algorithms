def permutations(letters):
  def dfs(start_index, path, used, res):
    if start_index == len(letters):
      res.append(''.join(path))
      return
    for i, letter in enumerate(letters):
      if used[i]:
        continue
      path.append(letter)
      print(path)
      used[i] = True
      dfs(start_index + 1, path, used, res)
      path.pop()
      used[i] = False
  res = []
  dfs(0, [], [False] * len(letters), res)
  return res

print(permutations('abc'))