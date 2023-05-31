def quicksort_middle_pivot_asc(arr):
  if len(arr) <= 1:
    return arr
  
  pivot = arr[len(arr) // 2]
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]
  return quicksort_middle_pivot_asc(left) + middle + quicksort_middle_pivot_asc(right)

def quicksort_middle_pivot_desc(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr) // 2]
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]
  return quicksort_middle_pivot_desc(right) + middle + quicksort_middle_pivot_desc(left)



arr = [5, 3, 1, 2, 4]
print(quicksort_middle_pivot_asc(arr))
print(quicksort_middle_pivot_desc(arr))

  
  