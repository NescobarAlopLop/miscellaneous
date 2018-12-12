"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
import unittest


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        idx = len(digits) - 1
        carry = 1
        while carry > 0 and idx >= 0:
            carry = int((digits[idx] + carry) / 10)
            digits[idx] = (digits[idx] + 1) % 10
            idx -= 1
        if carry > 0:
            return [carry] + digits
        return digits


class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_0(self):
        nums1 = [1,2,3]
        res = self.sol.plusOne(nums1)
        print("result: {}".format(res))
        self.assertEqual([1,2,4], res)

    def test_1(self):
        nums1 = [4,3,2,1]
        res = self.sol.plusOne(nums1)
        print("result: {}".format(res))
        self.assertEqual([4,3,2,2], res)

    def test_2(self):
        nums1 = [9]
        res = self.sol.plusOne(nums1)
        print("result: {}".format(res))
        self.assertEqual([1, 0], res)


if __name__ == '__main__':
    unittest.main()
