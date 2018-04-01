def interpolation_search(sample_space, value):
  # Interpolation search [O(log log n)]
  left = 0
  right = len(sample_space) - 1

  left_value, right_value = sample_space[left], sample_space[right]
  while left <= right and left_value <= value and value <= right_value:
    pos = int(left + (value - left_value) * (right - left) / (right_value - left_value))
    if sample_space[pos] == value:
        return pos

    if sample_space[pos] < value:
      left = pos + 1
    else:
      right = pos - 1

    left_value, right_value = sample_space[left], sample_space[right]

  return False # cannot find value in the list

def interpolation_search_recursive(sample_space, value, left=0, right=None):
  right = right if right is not None else len(sample_space) - 1
  # Interpolation search [O(log log n)]
  left_value, right_value = sample_space[left], sample_space[right]
  if left > right or left_value > value or value > right_value:
      return False

  pos = int(left + (value - left_value) * (right - left) / (right_value - left_value))
  if sample_space[pos] == value:
      return pos
  elif sample_space[pos] < value:
    return interpolation_search_recursive(sample_space, value, pos + 1, right)
  else:
    return interpolation_search_recursive(sample_space, value, left, pos - 1)
