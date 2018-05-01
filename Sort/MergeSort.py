# merge sort [O(n log n)]
def rmsort(array):
    n = len(array)
    if n == 1:
        return array

    a = rmsort(array[:n//2])
    b = rmsort(array[n//2:])
    return merge(a, b)


def merge(a, b):
    a_index, b_index = 0, 0
    a_len, b_len = len(a), len(b)
    result = []

    while a_index < a_len or b_index < b_len:
        if b_index == b_len or (a_index != a_len and a[a_index] <= b[b_index]):
            result.append(a[a_index])
            a_index += 1
        else:
            result.append(b[b_index])
            b_index += 1
    
    return result
