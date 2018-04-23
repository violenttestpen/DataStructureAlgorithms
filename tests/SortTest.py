import timeit

setup = '''
import random
array = list(range(1000))
random.shuffle(array)
'''

print(timeit.timeit('from Sort.InsertionSort import isort; isort(array)', setup=setup, number=100))
print(timeit.timeit('from Sort.MergeSort import rmsort; rmsort(array)', setup=setup, number=100))