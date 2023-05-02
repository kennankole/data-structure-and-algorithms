def bubble_sort_asc(arr):
  n = len(arr)
  for i in reversed(range(n)):
    swapped = False
    for j in range(i):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swapped = True
    if not swapped:
      return arr
  return arr


def bubble_sort_dsc(arr):
  n = len(arr)
  for i in reversed(range(n)):
    swapped = False
    for j in range(i):
      if arr[j] < arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swapped = True
    if not swapped:
      return arr
  return arr

arr = [5, 3, 1, 2, 4]
print(bubble_sort_asc(arr))
print(bubble_sort_dsc(arr))
