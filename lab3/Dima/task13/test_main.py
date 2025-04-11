import random
import time
import unittest
from main import main


class TestCase(unittest.TestCase):

    def test_simle(self):
        #given
        array_of_dots = [
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [1, 0, 1, 1],
            [1, 0, 1, 0],
        ]
        N, M = 4, 4

        #when
        tmp = time.time()

        answer = main(array_of_dots, N, M)

        tmp = time.time() - tmp

        #then
        self.assertLessEqual(tmp, 2)

    def test_max_gryadki(self):
        #given
        N, M = 200, 200
        array_of_dots = [[0 for _ in range(N)] for _ in range(M)]

        #when
        tmp = time.time()

        answer = main(array_of_dots, N, M)

        tmp = time.time() - tmp

        #then
        self.assertEqual(answer, 0)
        self.assertLessEqual(tmp, 2)

    def test_min_gryadki(self):
        #given
        N, M = 200, 200
        array_of_dots = [[1 for _ in range(N)] for _ in range(M)]

        #when
        tmp = time.time()

        answer = main(array_of_dots, N, M)

        tmp = time.time() - tmp

        #then
        self.assertEqual(answer, 1)
        self.assertLessEqual(tmp, 2)


if __name__ == '__main__':
    unittest.TestCase()
