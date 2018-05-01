# counting sort [O(n+k)]
def csort(array):
    a = array[:]
    k = max(array) + 1

    # calculate the frequencies of each value
    count = [0] * k
    for x in array:
        count[x] += 1

    # calculate the starting index of each value
    total = 0
    for i in range(k):
        old_count = count[i]
        count[i] += total
        total += old_count
    
    # copy to output array, preserving order of inputs with equal keys
    for x in array:
        a[count[x] - 1] = x
        count[x] -= 1

    return a
