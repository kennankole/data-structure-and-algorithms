def bubble_sort_asc(arr)
  n = arr.length
  (n - 1).downto(0) do |i|
    swapped = false
    (0).upto(i - 1) do |j|
      if arr[j] > arr[j + 1]
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swapped = true
      end
    end
    if not swapped
      arr
    end
  end
  arr
end

def bubble_sort_des(arr)
  n = arr.length
  (n - 1).downto(0) do |i|
    swapped = false
    (0).upto(i - 1) do |j|
      if arr[j] < arr[j + 1]
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swapped = true
      end
    end
    if not swapped
      arr
    end
  end
  arr
end
bubble_sort_asc([5, 3, 2, 4, 1])
bubble_sort_des([5, 3, 2, 4, 1])