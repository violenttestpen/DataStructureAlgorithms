# tree sort [O(n log n)]
from Miscellaneous.BinarySearchTree import BinarySearchTree

def tsort(array):
    tree = BinarySearchTree()
    for item in array:
        tree.insert(item)
    return tree.inorder()
