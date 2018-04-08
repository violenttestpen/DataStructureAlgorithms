def isearch(sample_space, value, debug=False):
  # Interpolation search [O(log log n)]
  left, right = 0, len(sample_space) - 1

  if debug:
    num_of_checks = 0

  left_value, right_value = sample_space[left], sample_space[right]
  while left <= right and left_value <= value and value <= right_value:
    pos = left + (value - left_value) * (right - left) // (right_value - left_value)

    if debug:
      num_of_checks += 1
      print(f"Checking value at position {pos}: {sample_space[pos]}")

    if sample_space[pos] == value:
        if debug:
          print(f"Number of Checks: {num_of_checks}")
        return pos
    elif sample_space[pos] < value:
      left = pos + 1
    else:
      right = pos - 1

    left_value, right_value = sample_space[left], sample_space[right]
  
  if debug:
    print(f"Number of Checks: {num_of_checks}")

  return False # cannot find value in the list

def isearch_recursive(sample_space, value, left=0, right=None, debug=False, num_of_checks=0):
  right = right or len(sample_space) - 1
  # Interpolation search [O(log log n)]
  left_value, right_value = sample_space[left], sample_space[right]
  if left > right or left_value > value or value > right_value:
      if debug:
        print(f"Number of Checks: {num_of_checks}")
      return False

  pos = left + (value - left_value) * (right - left) // (right_value - left_value)

  if debug:
      num_of_checks += 1
      print(f"Checking value at position {mid}: {sample_space[mid]}")

  if sample_space[pos] == value:
      if debug:
        print(f"Number of Checks: {num_of_checks}")
      return pos
  elif sample_space[pos] < value:
    return interpolation_search_recursive(sample_space, value, pos + 1, right, debug, num_of_checks)
  else:
    return interpolation_search_recursive(sample_space, value, left, pos - 1, debug, num_of_checks)
