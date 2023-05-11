def binary_search(arr, target)
  low = 0
  high = arr.length - 1
  while low <= high
    mid = low + (high - low) / 2
    if arr[mid] == target
      return arr[mid]
    elsif arr[mid] < target
      low = mid + 1
    else
      high = mid - 1
    end
  end
  -1
end

binary_search([1, 3, 5, 7, 8], 8)
