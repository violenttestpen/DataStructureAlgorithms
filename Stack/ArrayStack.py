class ArrayStack:
    def __init__(self):
        self.__data = []

    def isempty(self):
        return len(self.__data) == 0

    def search(self, key):
        return len(self.__data) - self.__data.index(key) if key in self.__data else None

    def peek(self):
        return self.__data[-1] if not self.isempty() else None

    def push(self, data):
        self.__data.append(data)

    def pop(self):
        return self.__data.pop() if not self.isempty() else None
