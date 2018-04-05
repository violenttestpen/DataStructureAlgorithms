class ArrayStack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        return self.data[-1] if not is_empty() else None

    def push(self, data)
        self.data.append(data)

    def pop(self):
        return self.data.pop() if not is_empty() else None
