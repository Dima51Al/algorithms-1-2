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

    def f(self, x):
        if self.value <= x:
            if self.right is None:
                return 0
            return self.right.f(x)
        if self.left is None:
            return self.value
        t = self.left.f(x)
        if t == 0:
            return self.value
        return t


if __name__ == '__main__':
    c = ['+ 1', '+ 3', '+ 3', '> 1', '> 2', '> 3', '+ 2', '> 1']

    tree = None

    for i in c:
        if i[0] == '+':
            x = int(i[2:])
            if tree is None:
                tree = BST(None, x)
            else:
                tree.add(x)
        elif i[0] == '>':
            x = int(i[2:])
            print(tree.f(x) if tree else 0)
