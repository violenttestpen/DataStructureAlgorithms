def binary_search(sample_space, value)
  # Binary search [O(log n)]
  left = 0
  right = sample_space.length - 1

  while left <= right
    mid = (left + right) / 2
    return true if sample_space[mid] == value

    if sample_space[mid] < value
      left = mid + 1
    else
      right = mid - 1
    end
  end

  return false # cannot find value in the list
end

def binary_search_recursive(sample_space, value, left = 0, right = sample_space.length - 1)
  # Binary search [O(log n)]
  return false unless left <= right
  
  mid = (left + right) / 2
  return true if sample_space[mid] == value
  return binary_search_recursive(sample_space, value, mid + 1, right) if sample_space[mid] < value
  return binary_search_recursive(sample_space, value, left, mid - 1) if sample_space[mid] > value
end
