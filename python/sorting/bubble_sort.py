def bubble_sort_asc(arr):
  n = len(arr)
  for i in reversed(range(n)):
    '''
    The outer loop iterates in reverse, 
    starting from the last element (n-1) 
    and going down to the first element (0). 
    This is optimization helps improve the algorithm's efficiency. 
    In the worst case, if the array is already sorted, 
    this modification can prevent unnecessary iterations.
    '''
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
    '''
    The outer loop iterates in reverse, 
    starting from the last element (n-1) 
    and going down to the first element (0). 
    This is optimization helps improve the algorithm's efficiency. 
    In the worst case, if the array is already sorted, 
    this modification can prevent unnecessary iterations.
    '''
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
