# insertion sort [O(n**2)]
def isort(array):
    a = array[:]

    # start from the second element
    for i in range(1, len(array)):
        # move left
        x = i - 1
        while x >= 0:
            if a[x] > a[x + 1]:
                a[x], a[x + 1] = a[x + 1], a[x]
            else:
                # all previous elements are assumed to be sorted already
                break
            x -= 1

    return a
