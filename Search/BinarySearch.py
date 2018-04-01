def binary_search(sample_space, value):
  # Binary search [O(log n)]
  left = 0
  right = len(sample_space) - 1

  while left <= right:
    mid = int((left + right) / 2)
    if sample_space[mid] == value:
        return mid

    if sample_space[mid] < value:
      left = mid + 1
    else:
      right = mid - 1

  return False # cannot find value in the list

def binary_search_recursive(sample_space, value, left=0, right=None):
  right = right if right is not None else len(sample_space) - 1
  # Binary search [O(log n)]
  if left > right:
      return False

  mid = int((left + right) / 2)
  if sample_space[mid] == value:
      return mid
  elif sample_space[mid] < value:
    return binary_search_recursive(sample_space, value, mid + 1, right)
  else:
    return binary_search_recursive(sample_space, value, left, mid - 1)
