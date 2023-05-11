def selection_sort_asc(arr)
  (0...arr.length).each do |i|
    min_idx = i
    (i...arr.length).each do |j|
      if arr[j] < arr[min_idx]
        min_idx = j 
      end
    end
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  end
  arr
end

def selection_sort_dsc(arr)
  (0...arr.length).each do |i|
    min_idx = i
    (i...arr.length).each do |j|
      if arr[j] > arr[min_idx]
        min_idx = j
      end
    end
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  end
  arr
end

selection_sort_asc([2, 90, 1, 4, 7, 3])
selection_sort_dsc([2, 90, 1, 4, 7, 3])
