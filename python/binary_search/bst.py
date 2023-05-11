def binary_search(arr, target):
  left = 0
  right = len(arr) - 1
  while left <= right:
    mid = left + (right - left) // 2
    if arr[mid] == target:
      return arr[mid]
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return - 1

arr = [1, 3, 5, 7, 8]
target = 5
print(binary_search(arr=arr, target=8))