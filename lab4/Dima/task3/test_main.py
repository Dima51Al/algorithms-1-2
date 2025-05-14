import time
import unittest
from main import rabin_karp_search


class TestNativeSearch(unittest.TestCase):

    def test_huge_string(self):
        start = time.time()
        result = rabin_karp_search("aba"*(10), "aba"*(10**6//3))
        finish = time.time()
        print(finish - start)
        self.assertLessEqual(finish - start, 2)
    def test_single_occurrence(self):
        result = rabin_karp_search("aba", "abaCaba")
        self.assertEqual(result, (2, [1, 5]))

    def test_no_occurrence(self):
        result = rabin_karp_search("abc", "defdef")
        self.assertEqual(result, (0, []))

    def test_empty_pattern(self):
        result = rabin_karp_search("", "abc")
        self.assertEqual(result, (0, []))

    def test_empty_text(self):
        result = rabin_karp_search("abc", "")
        self.assertEqual(result, (0, []))

    def test_both_empty(self):
        result = rabin_karp_search("", "")
        self.assertEqual(result, (0, []))


    def test_pattern_longer_than_text(self):
        result = rabin_karp_search("abcdef", "abc")
        self.assertEqual(result, (0, []))

    def test_exact_match(self):
        result = rabin_karp_search("hello", "hello")
        self.assertEqual(result, (1, [1]))


if __name__ == '__main__':
    unittest.main()
