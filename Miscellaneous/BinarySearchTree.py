class BinarySearchTree:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.node = BinaryNode(data)
        # self.data = data
        # self.left_child = left_child
        # self.right_child = right_child
    
    def search(self, data):
        node = self.node
        while node.data is not None and node.data != data:
            if data < node.data:
                node = node.left
            else:
                node = node.right
        return node
    
    def insert(self, data):
        node = self.node
        if node.data is None:
            node.data = data
        while node.data is not None and node.data != data:
            if data < node.data:
                node = node.left
            else:
                node = node.right

        if self.data is None:
            self.data = data
        elif data < self.data:
            if self.left_child is None:
                self.left_child = BinarySearchTree(data)
            else:
                self.left_child.insert(data)
        else:
            if self.right_child is None:
                self.right_child = BinarySearchTree(data)
            else:
                self.right_child.insert(data)
    
    def inorder(self):
        if self.left_child is None and self.right_child is None:
            return [self.data]
        
        result = []
        if self.left_child is not None:
            result += self.left_child.inorder()
        result.append(self.data)
        if self.right_child is not None:
            result += self.right_child.inorder()
        return result
