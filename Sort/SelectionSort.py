# selection sort [O(n**2)]
def ssort(array):
    a = array[:]

    # start from the second element
    for i in range(len(a) - 1):
        min_index = i
        for j in range(i + 1, len(a)):
            if a[min_index] > a[j]:
                min_index = j

        if min_index != i:
            a[min_index], a[i] = a[i], a[min_index]

    return a
