import unittest


class Solution:
    def is_unique_chars(self, s: str) -> bool:
        if len(s) > 256:
            return False
        image = [False] * 256
        for c in s:
            if image[ord(c)]:
                return False
            image[ord(c)] = True
        return True

    def is_unique_chars_bool(self, s: str) -> bool:
        if len(s) > 256:
            return False
        res = 0
        for c in s:
            if res & (1 << ord(c) - ord('A')):
                return False
            res |= 1 << ord(c) - ord('A')
        return True


class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_unique_chars_test_positive(self):
        self.assertTrue(self.sol.is_unique_chars('abcdef'))
        self.assertTrue(self.sol.is_unique_chars('f'))
        self.assertTrue(self.sol.is_unique_chars('bahfs'))

    def test_unique_chars_test_negative(self):
        self.assertFalse(self.sol.is_unique_chars('bahfss'))
        self.assertFalse(self.sol.is_unique_chars('AZA'))
        self.assertFalse(self.sol.is_unique_chars('kaaaa'))

    def test_unique_chars_bool_test_true(self):
        self.assertTrue(self.sol.is_unique_chars_bool('f'))
        self.assertTrue(self.sol.is_unique_chars_bool('bahfs'))

    def test_unique_chars_bool_test_false(self):
        self.assertFalse(self.sol.is_unique_chars_bool('bahfss'))
        self.assertFalse(self.sol.is_unique_chars_bool('AZA'))
        self.assertFalse(self.sol.is_unique_chars_bool('kaaaa'))


if __name__ == '__main__':
    unittest.main()
