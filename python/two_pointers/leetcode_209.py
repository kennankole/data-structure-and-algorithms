# https://leetcode.com/problems/minimum-size-subarray-sum/
def min_sub_arr_len(nums, target):
  size = len(nums) + 1
  total = 0
  left = 0
  for right in range(len(nums)):
    total += nums[right]
    while total >= target:
      size = min(size, right - left + 1)
      total -= nums[left]
      left += 1
  return size if size != len(nums) + 1 else 0

target = 7
nums = [2,3,1,2,4,3]
print(min_sub_arr_len(nums=nums, target=target))