from Miscellaneous import Node

class TreeLinkedList:
    def __init__(self):
        self.__head = None  # of type Node
    

    def append(self, data):
        # initialize the head if it's an empty LinkedList
        if self.head is None:
            self.head = Node(data)
        else:
            # traverse until the last node (next is nil)
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data)

    
    def prepend(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head
    
    
    def delete_with_value(self, data):
        # proceed only if there are values in the LinkedList
        if self.head is None:
            return None
        # special case if the head contains the value we wanted
        if self.head.data == data:
            self.head = self.head.next
    
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
            current = current.next
