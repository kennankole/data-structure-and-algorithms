# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/

class Solution:
  def __init__(self) -> None:
    pass
  
  def feasible(self, candies, k, num):
    '''
    The feasible function is designed to check whether 
    it's possible to allocate candies in a way that each child gets at least `num` candies. 
    The variable `count` is used to keep track of how many candies can be allocated with the current value of `num`.
    '''
    count = 0
    for i in range(len(candies)):
      # For each element in candies, we calculate how many piles of size `num` can be formed. 
      # We then add this `count` to the `count` variable.
      count += candies[i] // num

    # If the total count is greater than or equal to k. 
    # then it's feasible to allocate candies in a way that each child gets at least `num` candies
    return count >= k
  
  
  def maximum_candies(self, candies, k):
    low = 1
    high = max(candies)
    answer = 0
    while low <= high:
      mid = (low + high) // 2
      if self.feasible(candies, k, mid):
        answer = mid
        low = mid + 1
      else:
        high = mid - 1
    return answer
    
solution = Solution()
print(solution.maximum_candies([5,8,6], 3))
print(solution.maximum_candies([2, 5], 11))