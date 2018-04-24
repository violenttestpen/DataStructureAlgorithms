import collections

class PriorityQueue:
    def __init__(self):
        self.__data = collections.deque()
        self.__order = collections.deque()

    def isempty(self):
        return len(self.__data) == 0
    
    def search(self, key):
        return self.__data.index(key) if key in self.__data else None

    def peek(self):
        return self.__data[0] if not self.isempty() else None

    def enqueue(self, data, order):
        self.__data.append(data)
        self.__order.append(order)

        # Perform a single step insertion sort to move to correct priority [O(n)]
        for i in range(len(self.__order) - 1, 0, -1):
            if self.__order[i] < self.__order[i - 1]:
                self.__data[i], self.__data[i - 1] = self.__data[i - 1], self.__data[i]
                self.__order[i], self.__order[i - 1] = self.__order[i - 1], self.__order[i]

    def dequeue(self):
        if self.isempty():
            return None

        self.__order.popleft()
        return self.__data.popleft()
