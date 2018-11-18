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
import numpy as np
import unittest


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # print("#"*20)
        mat = np.zeros((len(s) + 2, len(s) + 2))
        for i in range(len(s)):
            mat[i][i] = True

        for i in range(len(s) - 1):
            mat[i][i+1] = s[i] == s[i + 1]

        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if not mat[i][j]:
                    mat[i][j] = mat[i + 1][j - 1] and s[i] == s[j]
                    # print(s[i:j + 1], mat[i][j])
        rv = ''
        # print("#"*20)
        for i in range(len(s)):
            for j in range(i, len(s)):
                if mat[i][j]:
                    if j - i >= len(rv):
                        rv = s[i:j + 1]
                        # print(rv)
        return rv


class TestMe(unittest.TestCase):
    sol = Solution()

    def test_babad(self):

        res = self.sol.longestPalindrome('babad')
        self.assertTrue(res == 'bab' or res == 'aba')

    # def test_cbbd(self):
        res = self.sol.longestPalindrome("cbbd")
        self.assertEqual(res, 'bb')

    # def test_a(self):
        res = self.sol.longestPalindrome("a")
        self.assertEqual(res, 'a')

    # def test_abcba(self):
        res = self.sol.longestPalindrome("abcba")
        self.assertEqual('abcba', res)


if __name__ == '__main__':
    # unittest.main()
    sol = Solution()
    res = sol.longestPalindrome('babad')
    print("result: {} - {}".format(res, res == 'bab' or res == 'aba'))
    res = sol.longestPalindrome("cbbd")
    print("result: {} - {}".format(res, res == 'bb'))
    res = sol.longestPalindrome("a")
    print("result: {} - {}".format(res, res == 'a'))
    res = sol.longestPalindrome("abcba")
    print("result: {} - {}".format(res, res == 'abcba'))
