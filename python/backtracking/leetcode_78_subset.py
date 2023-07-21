#https://leetcode.com/problems/subsets/
'''
Time Complexity: O(2^n)
Space Complexity: O(n)
'''
def subsets(nums):
  results = []
  curr_subset = []
  def dfs(i):
    print(i)
    if i >= len(nums):
      results.append(curr_subset.copy())
      return
    
    curr_subset.append(nums[i])
    dfs(i + 1)
    
    curr_subset.pop()
    dfs(i + 1)
  dfs(0)
  return results



def subsets_two(nums):
  results = []
  def dfs(i, path):
    print(i, path)
    if i == len(nums):
      results.append(path)
      return
    
    dfs(i + 1, path + [nums[i]])
    print('call me now')
    dfs(i + 1, path)
  dfs(0, [])
  return results
    
    
def subsets_three(nums):
  def dfs(i, path):
    results.append(path[:])
    for num_idx in range(i, len(nums)):
      path.append(nums[num_idx])
      dfs(num_idx + 1, path)
      path.pop()
  results = []
  dfs(0, [])
  return results

print(subsets_two([1, 2, 3]))
  