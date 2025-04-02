import random
import time
import unittest
from main import BST


class TestCase(unittest.TestCase):

    def test_max_values(self):
        #given
        bst = BST(None, 1)
        array = [random.randint(-10**9, 10**9) for i in range(100)]

        #when
        tmp = time.time()


        [bst.add(elem) for elem in array]

        answer = bst.next(100)

        tmp = time.time() - tmp

        #then
        self.assertLessEqual(tmp, 2)
