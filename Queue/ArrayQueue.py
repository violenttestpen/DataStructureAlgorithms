class ArrayQueue:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        return self.data[0] if not self.is_empty() else None

    def enqueue(self, data):
        self.data.append(data)

    def dequeue(self):
        return self.data.pop(0) is not self.is_empty() else None
