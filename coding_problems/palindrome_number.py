import unittest

"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


class Solution:
    # def isPalindrome0(self, x):
    #     tmp_x = x
    #     digits = 0
    #     while tmp_x:
    #         digits += 1
    #         tmp_x = int(tmp_x / 10)
    #     digits -= 1
    #     while x:
    #         left = int(x / 10 ** digits)
    #         right = x % 10
    #         if left != right:
    #             return False
    #         x /= 10
    #         x %= 10
    #         digits -= 1
    #     return True

    def isPalindrome0(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        return x == x[::-1]

    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        for b, e in zip(x, x[::-1]):
            if b != e:
                return False
        return True

    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        x_len = int(len(x))
        for i in range(int(x_len / 2)):
            if x[i] != x[x_len - i - 1]:
                return False
        return True


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_negative(self):
        self.assertFalse(self.solution.isPalindrome0(-121))
        self.assertFalse(self.solution.isPalindrome1(-121))
        self.assertFalse(self.solution.isPalindrome2(-121))

    def test_positive(self):
        self.assertTrue(self.solution.isPalindrome0(121))
        self.assertTrue(self.solution.isPalindrome1(121))
        self.assertTrue(self.solution.isPalindrome2(121))
        self.assertFalse(self.solution.isPalindrome0(10))
        self.assertFalse(self.solution.isPalindrome1(10))
        self.assertFalse(self.solution.isPalindrome2(10))


if __name__ == '__main__':
    unittest.main()
