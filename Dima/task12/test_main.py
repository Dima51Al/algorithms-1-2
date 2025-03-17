import random
import time
import unittest
from main import task12


class TestCase(unittest.TestCase):

    def test_max_values(self):
        #given
        n = 40000
        array = [random.randint(-10**8*2, i) for i in range(n)]

        #when
        tmp = time.time()

        answer = task12(array)

        tmp = time.time() - tmp

        #then
        self.assertLessEqual(tmp, 2)
