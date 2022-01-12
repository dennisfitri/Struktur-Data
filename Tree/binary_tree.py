class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def setLeft(self, data):
        self.left = Node(data)
    def setRight(self, data):
        self.right = Node(data)
    def show(self, level=0, prefix='-'):
        print('  ' * level, prefix, self.data)
        if self.left: self.left.show(level + 1, '<')
        if self.right: self.right.show(level + 1, '>')

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    def show(self):
        self.root.show()

tree = BinaryTree(Node(10))
tree.root.setLeft(4)
tree.root.setRight(7)
tree.root.left.setLeft(8)
tree.root.right.setLeft(6)
tree.root.right.setRight(2)
tree.root.right.left.setRight(3)
tree.show()