class BST:
    def __init__(self, par, v):
        self.par = par
        self.value = v
        self.left = None
        self.right = None

    def add(self, v):
        if v < self.value:
            if self.left is None:
                self.left = BST(self, v)
            else:
                self.left.add(v)
        elif v > self.value:
            if self.right is None:
                self.right = BST(self, v)
            else:
                self.right.add(v)

    def find(self, v):
        if v == self.value:
            return self
        elif v < self.value and self.left:
            return self.left.find(v)
        elif v > self.value and self.right:
            return self.right.find(v)
        return None

    def exists(self, v):
        return "true" if self.find(v) else "false"
    

    def delete(self, v):
        node = self.find(v)
        if node is None:
            return

        def transplant(u, v):
            if u.par is None:
                return v
            if u == u.par.left:
                u.par.left = v
            else:
                u.par.right = v
            if v:
                v.par = u.par
            return self

        if node.left is None:
            return transplant(node, node.right)
        elif node.right is None:
            return transplant(node, node.left)

        y = node.right
        while y.left:
            y = y.left
        if y.par != node:
            transplant(y, y.right)
            y.right = node.right
            y.right.par = y
        transplant(node, y)
        y.left = node.left
        y.left.par = y
        return self

    def next(self, x):
        node = self.find(x)
        if node and node.right:
            node = node.right
            while node.left:
                node = node.left
            return node.value

        succ = None
        root = self
        while root:
            if root.value > x:
                succ = root.value
                root = root.left
            else:
                root = root.right
        if succ:
            return succ
        return "none"


    def prev(self, x):
        node = self.find(x)
        if node and node.left:
            node = node.left
            while node.right:
                node = node.right
            return node.value

        pred = None
        root = self
        while root:
            if root.value < x:
                pred = root.value
                root = root.right
            else:
                root = root.left
        return pred if pred is not None else "none"


if __name__ == "__main__":
    root = BST(None, 2)
    root.add(5)
    root.add(3)

    print(root.exists(2))  # true
    print(root.exists(4))  # false
    print(root.next(4))  # 5
    print(root.prev(4))  # 3
    root.delete(5)
    print(root.next(4))  # none
    print(root.prev(4))  # 3