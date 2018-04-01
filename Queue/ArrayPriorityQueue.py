class ArrayPriorityQueue:
    def __init__(self):
        self.data = []
        self.order = []

    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        return self.data[0] if not self.is_empty() else None

    def enqueue(self, data, order):
        self.data.append(data)
        self.order.append(order)

        # Perform a single step insertion sort to move to correct priority [O(n)]
        i = len(self.order) - 1
        while i > 0:
            if self.order[i] < self.order[i - 1]:
                self.data[i], self.data[i - 1] = self.data[i - 1], self.data[i]
                self.order[i], self.order[i - 1] = self.order[i - 1], self.order[i]
            i -= 1

    def dequeue(self):
        if self.is_empty():
            return None

        self.order.pop()
        return self.data.pop(0)
