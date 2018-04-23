def bsearch(sample_space, value, debug=False):
  # Binary search [O(log n)]
  left, right = 0, len(sample_space) - 1

  if debug:
    num_of_checks = 0

  while left <= right:
    mid = (left + right) // 2

    if debug:
      num_of_checks += 1
      print(f"Checking value at position {mid}: {sample_space[mid]}")

    if sample_space[mid] == value:
        if debug:
          print(f"Number of Checks: {num_of_checks}")
        return mid
    elif sample_space[mid] < value:
      left = mid + 1
    else:
      right = mid - 1

  if debug:
    print(f"Number of Checks: {num_of_checks}")

  return False # cannot find value in the list

def rbsearch(sample_space, value, left=0, right=None, debug=False, num_of_checks=0):
  right = right or len(sample_space) - 1
  # Binary search [O(log n)]
  if left > right:
      if debug:
        print(f"Number of Checks: {num_of_checks}")
      return False
    
  mid = (left + right) // 2

  if debug:
      num_of_checks += 1
      print(f"Checking value at position {mid}: {sample_space[mid]}")

  if sample_space[mid] == value:
      if debug:
        print(f"Number of Checks: {num_of_checks}")
      return mid
  elif sample_space[mid] < value:
    return bsearch_recursive(sample_space, value, mid + 1, right, debug, num_of_checks)
  else:
    return bsearch_recursive(sample_space, value, left, mid - 1, debug, num_of_checks)
