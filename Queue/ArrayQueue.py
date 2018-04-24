class ArrayQueue:
    def __init__(self):
        self.__data = []

    def isempty(self):
        return self.__data == []

    def search(self, key):
        return self.__data.index(key) if key in self.__data else None

    def peek(self):
        return self.__data[0] if not self.isempty() else None

    def enqueue(self, data):
        self.__data.append(data)

    def dequeue(self):
        return self.__data.pop(0) if not self.isempty() else None
