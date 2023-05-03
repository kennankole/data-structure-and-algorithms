def sorting_list_asc(arr):
  for idx, val in enumerate(arr):
    current_idx = idx
    while current_idx > 0 and arr[current_idx] < arr[current_idx - 1]:
      arr[current_idx], arr[current_idx - 1] = arr[current_idx - 1], arr[current_idx]
      current_idx -= 1
  return arr

def sorting_list_dsc(arr):
  for idx, value in enumerate(arr):
    current_idx = idx
    while current_idx > 0 and arr[current_idx] > arr[current_idx - 1]:
      arr[current_idx - 1], arr[current_idx] = arr[current_idx], arr[current_idx - 1]
      current_idx -= 1
  return arr

arr = [5, 3, 1, 2, 4]
print(sorting_list_asc(arr=arr))
print(sorting_list_dsc(arr=arr))
