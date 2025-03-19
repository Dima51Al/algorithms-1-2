import random
import time
import unittest
from main import main


class TestCase(unittest.TestCase):

    def test_max_values(self):
        #given
        K = 1000
        n = 500
        array = [random.randint(1, 100) for i in range(n)]

        #when
        tmp = time.time()

        answer = main(K, n, array)

        tmp = time.time() - tmp

        #then
        self.assertLessEqual(tmp, 2)
