"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit
signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your
function returns 0 when the reversed integer overflows.
"""
import unittest


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        min = -2 ** 31
        max = 2 ** 31 - 1
        sign = 1
        if x < 0:
            sign = -1
            x *= sign
        res = 0
        while x:
            res *= 10
            res += x % 10
            x //= 10
        if min < res < max:
            return res * sign
        return 0


class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_0(self):
        num = 123
        res = self.sol.reverse(num)
        print("result: {}".format(res))
        self.assertEqual(res, 321)

    def test_1(self):
        num = -123
        res = self.sol.reverse(num)
        print("result: {}".format(res))
        self.assertEqual(res, -321)

    def test_2(self):
        num = 120
        res = self.sol.reverse(num)
        print("result: {}".format(res))
        self.assertEqual(res, 21)


if __name__ == '__main__':
    unittest.main()
