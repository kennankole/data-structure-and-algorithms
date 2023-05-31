def merge_sort(arr)
  n = arr.length
  if n <= 1
    return arr
  end

  midpoint = n.div(2)
  left_array = merge_sort(arr[0...midpoint])
  right_array = merge_sort(arr[midpoint..n])
  results = []
  left_p = 0
  right_p = 0
  while left_p < midpoint || right_p < n - midpoint
    if left_p == midpoint
      results << right_array[right_p]
      right_p += 1
    elsif right_p == n - midpoint
      results << left_array[left_p]
      left_p += 1
    elsif left_array[left_p] < right_array[right_p]
      results << left_array[left_p]
      left_p += 1
    else
      results << right_array[right_p]
      right_p += 1
    end
  end
  results
end

arr = [5, 1, 4, 2, 3]
print merge_sort(arr)

#arr[0..midpoint]:
# This range is inclusive of the midpoint.

# arr[0...midpoint]:
# The range is exclusive of the midpoint