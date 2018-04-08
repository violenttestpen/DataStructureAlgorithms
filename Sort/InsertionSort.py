# insertion sort [O(n**2)]
def isort(array, debug=False):
    a = array[:]
    if debug:
        num_of_comparisons = 0
        num_of_swaps = 0
        num_of_iterations = 0

    # start from the second element
    for i in range(1, len(array)):
        # move left
        x = i - 1
        while x >= 0:
            if debug:
                num_of_comparisons += 1
                print(f"Comparison step: {a[x]} > {a[x + 1]}")
            
            if a[x] > a[x + 1]:
                if debug:
                    num_of_swaps += 1
                    print(f"Swap step: {a[x]}, {a[x + 1]}")
                a[x], a[x + 1] = a[x + 1], a[x]
            else:
                # all previous elements are assumed to be sorted already
                break
            x -= 1

        if debug:
            num_of_iterations += 1
            print(f"Output step: {a}")

    if debug:
        print(f"Number of Iterations: {num_of_iterations}")
        print(f"Number of Comparisons: {num_of_comparisons}")
        print(f"Number of Swaps: {num_of_swaps}")
    return a
