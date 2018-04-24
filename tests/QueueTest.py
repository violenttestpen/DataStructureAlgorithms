import timeit

list_size = 1000
number = 100

setup = f'''
import random
array = list(range({list_size}))
random.shuffle(array)
def run_queue(queue):
    for i in array:
        queue.enqueue(i)
    for i in array:
        queue.dequeue()
def run_priority_queue(queue):
    for i in array:
        queue.enqueue(i, i)
    for i in array:
        queue.dequeue()
'''

print(f'ArrayQueue for array of size {list_size} ({number} iterations)')
print('Time taken: %.2fs' % timeit.timeit('from Queue.ArrayQueue import ArrayQueue; run_queue(ArrayQueue())', setup=setup, number=number))
print(f'Queue for array of size {list_size} ({number} iterations)')
print('Time taken: %.2fs' % timeit.timeit('from Queue.Queue import Queue; run_queue(Queue())', setup=setup, number=number))
print(f'ArrayPriorityQueue for array of size {list_size} ({number} iterations)')
print('Time taken: %.2fs' % timeit.timeit('from Queue.ArrayPriorityQueue import ArrayPriorityQueue; run_priority_queue(ArrayPriorityQueue())', setup=setup, number=number))
print(f'PriorityQueue for array of size {list_size} ({number} iterations)')
print('Time taken: %.2fs' % timeit.timeit('from Queue.PriorityQueue import PriorityQueue; run_priority_queue(PriorityQueue())', setup=setup, number=number))
