# selection sort [O(n**2)]
def ssort(array, debug=False):
    a = array[:]
    if debug:
        num_of_comparisons = 0
        num_of_swaps = 0
        num_of_iterations = 0

    # start from the second element
    for i in range(len(a) - 1):
        min_index = i
        for j in range(i + 1, len(a)):
            if debug:
                num_of_comparisons += 1
                print(f"Comparison step: {a[min_index]} > {a[j]}")
            if a[min_index] > a[j]:
                min_index = j

        if min_index != i:
            if debug:
                num_of_swaps += 1
                print(f"Swap step: {a[i]}, {a[min_index]}")
            a[min_index], a[i] = a[i], a[min_index]

        if debug:
            num_of_iterations += 1
            print(f"Output step: {a}")

    if debug:
        print(f"Number of Iterations: {num_of_iterations}")
        print(f"Number of Comparisons: {num_of_comparisons}")
        print(f"Number of Swaps: {num_of_swaps}")
    return a
