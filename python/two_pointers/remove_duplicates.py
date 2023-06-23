def remove_duplicates(arr):
  low = 0
  for fast in range(len(arr)):
    if arr[fast] != arr[low]:
      low += 1
      arr[low] = arr[fast]
  return arr[:low + 1]

print(remove_duplicates([0, 0, 1, 1, 1, 2, 2]))