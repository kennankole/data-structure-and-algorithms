#https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/
'''
Given a binary array data, return the minimum number of swaps required to group all 1’s present 
in the array together in any place in the array.

Example 1:

Input: data = [1,0,1,0,1]
Output: 1
Explanation: There are 3 ways to group all 1's together: [1,1,1,0,0] using 1 swap. 
[0,1,1,1,0] using 2 swaps. [0,0,1,1,1] using 1 swap. The minimum is 1.

Example 2:

Input: data = [0,0,0,1,0]
Output: 0
Explanation: Since there is only one 1 in the array, no swaps are needed.

Example 3:

Input: data = [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].

Constraints:

1 <= data.length <= 105
data[i] is either 0 or 1.
'''
def min_swaps(data):
  count_ones = data.count(1)
  total = 0
  for i in range(count_ones):
    total += data[i]
  swap = count_ones - total
  for right in range(count_ones, len(data)):
    total += data[right]
    total -= data[right - count_ones]
    swap = min(swap, count_ones - total)
  return swap
  
nums = [1,1,0,0,1]
print(min_swaps(nums))