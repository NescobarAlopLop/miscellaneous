"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
"""
import unittest


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        b, e = 0, len(s) - 1
        while b < e:
            while b < e and not s[b].isalnum():
                b += 1
            while b < e and not s[e].isalnum():
                e -= 1
            if s[b].lower() != s[e].lower():
                return False
            b += 1
            e -= 1
        return True


class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_0(self):
        s = "A man, a plan, a canal: Panama"
        res = self.sol.isPalindrome(s)
        print("result: {}".format(res))
        self.assertTrue(res)

    def test_1(self):
        s = "race a car"
        res = self.sol.isPalindrome(s)
        print("result: {}".format(res))
        self.assertFalse(res)

    def test_2(self):
        s = ".,"
        res = self.sol.isPalindrome(s)
        print("result: {}".format(res))
        self.assertTrue(res)

    def test_3(self):
        s = "0P"
        res = self.sol.isPalindrome(s)
        print("result: {}".format(res))
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()
