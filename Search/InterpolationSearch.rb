def interpolation_search(sample_space, value)
  # Interpolation search [O(log log n)]
  left = 0
  right = sample_space.length - 1

  while left <= right && (left_value = sample_space[left]) <= value && value <= (right_value = sample_space[right])
    pos = left + (value - left_value) * (right - left) / (right_value - left_value)
    return true if sample_space[pos] == value
    
    if sample_space[pos] < value
      left = pos + 1
    else
      right = pos - 1
    end
  end
  
  return false # cannot find value in the list
end

def interpolation_search_recursive(sample_space, value, left = 0, right = sample_space.length - 1)
  # Interpolation search [O(log log n)]
  return false unless left <= right && (left_value = sample_space[left]) <= value && value <= (right_value = sample_space[right])
  
  pos = left + (value - left_value) * (right - left) / (right_value - left_value)
  return true if sample_space[pos] == value
  return interpolation_search_recursive(sample_space, value, pos + 1, right) if sample_space[pos] < value
  return interpolation_search_recursive(sample_space, value, left, pos - 1) if sample_space[pos] > value
end