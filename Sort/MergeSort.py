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
    result = []

    while a_index < len(a) or b_index < len(b):
        if b_index == len(b) or (a_index != len(a) and a[a_index] <= b[b_index]):
            result.append(a[a_index])
            a_index += 1
        else:
            result.append(b[b_index])
            b_index += 1
    
    return result
