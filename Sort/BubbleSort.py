# bubble sort [O(n**2)]
def bsort(array, debug=False):
    a = array[:]
    if debug:
        num_of_comparisons = 0
        num_of_swaps = 0
        num_of_iterations = 0

    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if debug:
                num_of_comparisons += 1
                print(f"Comparison step: {a[j]} > {a[j + 1]}")
            if a[j] > a[j + 1]:
                if debug:
                    num_of_swaps += 1
                    print(f"Swap step: {a[j]}, {a[j + 1]}")
                a[j], a[j + 1] = a[j + 1], a[j]

        if debug:
            num_of_iterations += 1
            print(f"Output step: {a}")
    
    if debug:
        print(f"Number of Iterations: {num_of_iterations}")
        print(f"Number of Comparisons: {num_of_comparisons}")
        print(f"Number of Swaps: {num_of_swaps}")
    return a
