"""
Implement countAndSay().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

"""
import unittest


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_0(self):
        res = self.sol.strStr(haystack="hello", needle="ll")
        self.assertEqual(2, res)
        res = self.sol.strStr(haystack="hee649*/23llo", needle="llo")
        self.assertEqual(10, res)

    def test_1(self):
        res = self.sol.strStr(haystack="aaaaa", needle="bba")
        self.assertEqual(-1, res)
        res = self.sol.strStr(haystack="aaaaa", needle="")
        self.assertEqual(0, res)
        res = self.sol.strStr(haystack="mississippi", needle="a")
        self.assertEqual(-1, res)


if __name__ == '__main__':
    unittest.main()
