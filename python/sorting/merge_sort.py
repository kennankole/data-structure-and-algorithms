def sort_list_asc(arr):
  n = len(arr)
  if n <= 1:
    return arr
  midpoint = n // 2
  left, right = sort_list_asc(arr[:midpoint]), sort_list_asc(arr[midpoint:])
  result_list = []
  left_pointer, right_pointer = 0, 0
  while left_pointer < midpoint or right_pointer < n - midpoint:
    # reached the end of the left half of the array
    # add elements from the right half 
    if left_pointer == midpoint:
      result_list.append(right[right_pointer])
      right_pointer += 1
      
    # reached the end of the right half of the array, 
    # add elements from the left half
    elif right_pointer == n - midpoint:
      result_list.append(left[left_pointer])
      left_pointer += 1
    
    elif left[left_pointer] <= right[right_pointer]:
      result_list.append(left[left_pointer])
      left_pointer += 1
    
    else:
      result_list.append(right[right_pointer])
      print('I am first to be sorted')
      print(result_list)
      right_pointer += 1
  return result_list

def merge_sort_asc(arr):
  if len(arr) > 1:
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    merge_sort_asc(left_half)
    merge_sort_asc(right_half)
    
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
      if left_half[i] < right_half[j]:
        arr[k] = left_half[i]
        i += 1
      else:
        arr[k] = right_half[j]
        j += 1
      k += 1
      
    while i < len(left_half):
      arr[k] = left_half[i]
      i += 1
      k += 1
    
    while j < len(right_half):
      arr[k] = right_half[j]
      j += 1
      k += 1
  return arr


def merge_sort_desc(arr):
  if len(arr) > 1:
    midpoint = len(arr) // 2
    left_half = arr[midpoint:]
    right_half = arr[:midpoint]
    
    merge_sort_desc(left_half)
    merge_sort_desc(right_half)
    
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
      if left_half[i] > right_half[j]:
        arr[k] = left_half[i]
        i += 1
      else:
        arr[k] = right_half[j]
        j += 1
      k += 1
    
    while i < len(left_half):
      arr[k] = left_half[i]
      i += 1
      k += 1
    
    while j < len(right_half):
      arr[k] = right_half[j]
      j += 1
      k += 1
  return arr
      
      
      
arr = [5, 3, 1, 2, 4]
print(merge_sort_desc(arr))
print(merge_sort_asc(arr))