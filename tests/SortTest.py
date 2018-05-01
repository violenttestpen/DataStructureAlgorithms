import timeit

list_size = 1000
number = 100

setup_random = f'''
import random
array = list(range({list_size}))
random.shuffle(array)
'''

setup_reversed = f'''
array = list(range({list_size}, 0, -1))
'''

setup_nearly_sorted = f'''
import random
array = list(range({list_size}))
iterations = {list_size // 20}
for i in range(iterations):
    x = random.randint(0, {list_size})
    y = random.randint(0, {list_size})
    while x == y:
        y = random.randint(0, {list_size})
    array[x], array[y] = array[y], array[x]
'''

setup_sorted = f'''
array = list(range({list_size}))
'''

def runit(setup, number, description='Test:'):
    print(description)
    #print(f'TreeSort for array of size {list_size} ({number} iterations)')
    #print('Time taken: %.2fs' % timeit.timeit('from Sort.TreeSort import tsort; tsort(array)', setup=setup, number=number))
    print(f'BubbleSort for array of size {list_size} ({number} iterations)')
    print('Time taken: %.2fs' % timeit.timeit('from Sort.BubbleSort import bsort; bsort(array)', setup=setup, number=number))
    print(f'SelectionSort for array of size {list_size} ({number} iterations)')
    print('Time taken: %.2fs' % timeit.timeit('from Sort.SelectionSort import ssort; ssort(array)', setup=setup, number=number))
    print(f'InsertionSort for array of size {list_size} ({number} iterations)')
    print('Time taken: %.2fs' % timeit.timeit('from Sort.InsertionSort import isort; isort(array)', setup=setup, number=number))
    print(f'MergeSort for array of size {list_size} ({number} iterations)')
    print('Time taken: %.2fs' % timeit.timeit('from Sort.MergeSort import rmsort; rmsort(array)', setup=setup, number=number))
    print(f'CountingSort for array of size {list_size} ({number} iterations)')
    print('Time taken: %.2fs' % timeit.timeit('from Sort.CountingSort import csort; csort(array)', setup=setup, number=number))
    print()

runit(setup_random, number, 'Random Array Test:')
runit(setup_reversed, number, 'Reversed Array Test:')
runit(setup_nearly_sorted, number, 'Sorted Array Test:')
runit(setup_sorted, number, 'Sorted Array Test:')
