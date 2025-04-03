import sys # again I need it just to more effective input

class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None # all values in left subtree are less than value in root
        self.right = None # all values in right subtree are bigger than value in root
        self.size = 1 # amount of nodes in subtree

class BST:
    def __init__(self):
        self.root = None # root is empty now

    def _update_size(self, node): # private method that updates tree size for current Node
        if node:
            node.size = 1 + (node.left.size if node.left else 0) + (node.right.size if node.right else 0) # if node has sons, new size = 1 + amount of sons in left subtree + amount of sons in right subtree

    def _insert(self, node, value): # recursive private methode to add element to tree
        if not node:
            return Node(value) # if we find empty space create new node
        if value < node.value: # main rule of BST
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        self._update_size(node)
        return node # we return node to safe tree structure

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _find_kth(self, node, k): # method to find kth element in the tree for "?" command
        left_size = node.left.size if node.left else 0
        if k == left_size + 1:
            return node.value
        elif k <= left_size: # recursively find in left subtree
            return self._find_kth(node.left, k)
        else:
            return self._find_kth(node.right, k - left_size - 1) # recursively find in right subtree

    def find_kth(self, k):
        return self._find_kth(self.root, k)


bst = BST()

input_data = sys.stdin.read().strip().split('\n')
output = []

for line in input_data:
    parts = line.split()
    if parts[0] == '+':
        bst.insert(int(parts[1]))
    elif parts[0] == '?':
        output.append(str(bst.find_kth(int(parts[1]))))

sys.stdout.write('\n'.join(output) + '\n')
