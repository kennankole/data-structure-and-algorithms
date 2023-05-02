def selection_sort_asc(arr):
  for idx in range(len(arr)):
    minimum = idx
    for idx_inner in range(idx, len(arr)):
      if arr[idx_inner] < arr[minimum]:
        minimum = idx_inner
    arr[idx], arr[minimum] = arr[minimum], arr[idx]
  return arr


def selection_sort_dsc(arr):
  for i in range(len(arr)):
    min_index = i
    for j in range(i, len(arr)):
      if arr[j] > arr[min_index]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
  return arr

print(selection_sort_asc([5, 3, 1, 2, 4]))
print(selection_sort_dsc([5, 3, 1, 2, 4]))