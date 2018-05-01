def bsearch(sample_space, value):
    # Binary search [O(log n)]
    left, right = 0, len(sample_space) - 1

    while left <= right:
        mid = (left + right) // 2

        if sample_space[mid] == value:
            return mid
        elif sample_space[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return False # cannot find value in the list


def rbsearch(sample_space, value, left=0, right=None):
    right = right or len(sample_space) - 1
    # Binary search [O(log n)]
    if left > right:
        return False
    
    mid = (left + right) // 2

    if sample_space[mid] == value:
          return mid
    elif sample_space[mid] < value:
        return rbsearch(sample_space, value, mid + 1, right)
    else:
        return rbsearch(sample_space, value, left, mid - 1)
