'''
Given an array of integers, 
move all the 0s to the back of the array while maintaining the relative order 
of the non-zero elements. Do this in-place using constant auxiliary space.

Input:

[1, 0, 2, 0, 0, 7]
Output:

[1, 2, 7, 0, 0, 0]
'''

def move_non_zero(arr):
  low = 0
  for fast in range(len(arr)):
    if arr[fast] != 0:
      arr[low], arr[fast] = arr[fast], arr[low]
      low += 1
  return arr

def move_zeros(arr):
  non_zeros = []
  for n in arr:
    if n != 0:
      non_zeros.append(n)
  
  i = 0
  while i < len(non_zeros):
    arr[i] = non_zeros[i]
    i += 1
  while i < len(arr):
    arr[i] = 0
    i += 1
  return arr
  
print(move_zeros([1, 0, 2, 0, 0, 7]))