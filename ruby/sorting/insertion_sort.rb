def insertion_sort_ascending(arr)
  arr.each_with_index do |value, idx|
    current_idx = idx
    while current_idx.positive? && arr[current_idx] < arr[current_idx - 1]
      arr[current_idx], arr[current_idx - 1] = arr[current_idx - 1], arr[current_idx]
      current_idx -= 1
    end
  end
  arr
end
insertion_sort_ascending([5, 2, 1, 4, 9])
