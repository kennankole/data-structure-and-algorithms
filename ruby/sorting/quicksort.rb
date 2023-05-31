def quicksort(arr)
  if arr.length <= 1 
    return arr
  end
  midpoint = arr.length.div(2)
  pivot = arr[midpoint]
  left = []
  right = []
  equal = []
  arr.each do |num|
    if num < pivot
      left << num
    elsif num > pivot
      right << num
    else
      equal << num
    end
  end
  return quicksort(left) + equal + quicksort(right)
end

print quicksort([5, 1, 4, 2, 3])