import sys # for fast reading huge amount of data

class BinaryTree: # just a way to store data
    def __init__(self, n, nodes):
        self.n = n
        self.nodes = nodes

    def in_order(self, index=0): # left brunch, root, right brunch
        if index == -1:
            return [] # our tree was ended
        left, right = self.nodes[index][1], self.nodes[index][2]
        return self.in_order(left) + [self.nodes[index][0]] + self.in_order(right) # result of left brunch + value of root + result of right brunch

    def pre_order(self, index=0): # root, left brunch, right brunch
        if index == -1:
            return []
        left, right = self.nodes[index][1], self.nodes[index][2]
        return [self.nodes[index][0]] + self.pre_order(left) + self.pre_order(right)

    def post_order(self, index=0): # left brunch, right brunch, root
        if index == -1:
            return []
        left, right = self.nodes[index][1], self.nodes[index][2]
        return self.post_order(left) + self.post_order(right) + [self.nodes[index][0]]


def main():
    n = int(sys.stdin.readline().strip())
    points = [tuple(map(int, sys.stdin.readline().split())) for i in range(n)] # Ki - value of point, Li - index of left son, Ri - index of right son
    tree = BinaryTree(n, points)

    print(" ".join(map(str, tree.in_order())))
    print(" ".join(map(str, tree.pre_order())))
    print(" ".join(map(str, tree.post_order())))

if __name__ == "__main__":
    main()
