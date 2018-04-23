import timeit

list_size = 1000
number = 100

setup = f'''
import random
array = list(range({list_size}))
random.shuffle(array)
'''

print(f'BubbleSort for array of size {list_size} ({number} iterations)')
print('Time taken: %.2fs' % timeit.timeit('from Sort.BubbleSort import bsort; bsort(array)', setup=setup, number=number))
print(f'SelectionSort for array of size {list_size} ({number} iterations)')
print('Time taken: %.2fs' % timeit.timeit('from Sort.SelectionSort import ssort; ssort(array)', setup=setup, number=number))
print(f'InsertionSort for array of size {list_size} ({number} iterations)')
print('Time taken: %.2fs' % timeit.timeit('from Sort.InsertionSort import isort; isort(array)', setup=setup, number=number))
print(f'MergeSort for array of size {list_size} ({number} iterations)')
print('Time taken: %.2fs' % timeit.timeit('from Sort.MergeSort import rmsort; rmsort(array)', setup=setup, number=number))