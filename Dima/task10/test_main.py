import random
import time
import unittest
from main import task10


class TestCase(unittest.TestCase):

    def test_max_values(self):
        #given

        n = 1000
        array = [[random.randint(1, 5), random.randint(-5, 5), i] for i in range(n)]

        #when
        tmp = time.time()

        answer = task10(1000, array)

        tmp = time.time() - tmp

        #then
        self.assertLessEqual(tmp, 2)
