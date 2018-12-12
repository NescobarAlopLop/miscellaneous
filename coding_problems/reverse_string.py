"""
Write a function that takes a string as input and returns the string reversed.

Example 1:
Input: "hello"
Output: "olleh"

Example 2:
Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"
"""
import unittest


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_0(self):
        s = "hello"
        res = self.sol.reverseString(s)
        print("result: {}".format(res))
        self.assertEqual(res, "olleh")

    def test_1(self):
        s = "A man, a plan, a canal: Panama"
        res = self.sol.reverseString(s)
        print("result: {}".format(res))
        self.assertEqual(res, "amanaP :lanac a ,nalp a ,nam A")


if __name__ == '__main__':
    unittest.main()
