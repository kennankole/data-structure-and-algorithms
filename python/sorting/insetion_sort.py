def sorting_list(arr):
  for idx, val in enumerate(arr):
    current_idx = idx
    while current_idx > 0 and arr[current_idx] < arr[current_idx - 1]:
      arr[current_idx], arr[current_idx - 1] = arr[current_idx - 1], arr[current_idx]
      current_idx -= 1
  return arr

arr = [5, 3, 1, 2, 4]
print(sorting_list(arr=arr))