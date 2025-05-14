import time
import unittest
from main import native_search


class TestNativeSearch(unittest.TestCase):

    def test_huge_string(self):
        start = time.time()
        result = native_search("aba"*10**4, "abaaba"*10**4)
        finish = time.time()
        self.assertLessEqual(finish - start, 2)
    def test_single_occurrence(self):
        result = native_search("aba", "abaCaba")
        self.assertEqual(result, (2, [1, 5]))

    def test_no_occurrence(self):
        result = native_search("abc", "defdef")
        self.assertEqual(result, (0, []))

    def test_empty_pattern(self):
        result = native_search("", "abc")
        self.assertEqual(result, (0, []))

    def test_empty_text(self):
        result = native_search("abc", "")
        self.assertEqual(result, (0, []))

    def test_both_empty(self):
        result = native_search("", "")
        self.assertEqual(result, (0, []))


    def test_pattern_longer_than_text(self):
        result = native_search("abcdef", "abc")
        self.assertEqual(result, (0, []))

    def test_exact_match(self):
        result = native_search("hello", "hello")
        self.assertEqual(result, (1, [1]))


if __name__ == '__main__':
    unittest.main()
