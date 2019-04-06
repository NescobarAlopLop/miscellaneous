#####@@@!/usr/bin/env python3
"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
"""
import unittest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) > 0:
            rv = s[0]
        else:
            return ""

        for i in range(1, len(s)):
            left_idx = i - 1
            right_idx = i
            while left_idx >=0 and right_idx < len(s) and s[left_idx] == s[right_idx]:
                if right_idx - left_idx + 1 > len(rv):
                    rv = s[left_idx:right_idx + 1]
                right_idx += 1
                left_idx -= 1

            left_idx = i - 1
            right_idx = i + 1
            while left_idx >= 0 and right_idx < len(s) and s[left_idx] == s[right_idx]:
                if right_idx - left_idx + 1 > len(rv):
                    rv = s[left_idx:right_idx + 1]
                right_idx += 1
                left_idx -= 1

        return rv


class TestMe(unittest.TestCase):
    sol = Solution()

    def test_babad(self):

        res = self.sol.longestPalindrome('babad')
        self.assertTrue(res == 'bab' or res == 'aba')

    def test_cbbd(self):
        res = self.sol.longestPalindrome("cbbd")
        self.assertEqual(res, 'bb')

    def test_a(self):
        res = self.sol.longestPalindrome("a")
        self.assertEqual(res, 'a')

    def test_abcba(self):
        res = self.sol.longestPalindrome("abcba")
        self.assertEqual('abcba', res)

    def test_empty(self):
        res = self.sol.longestPalindrome('')
        self.assertEqual('', res)


if __name__ == '__main__':
    unittest.main()
