"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4


"""
from unittest import TestCase


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = 0
        for n in nums:
            res = res ^ n
        return res


class TestSolution(TestCase):
    sol = Solution()

    def test_0(self):
        nums = [2,2,1]
        res = self.sol.singleNumber(nums)
        print("result: {}".format(res))
        self.assertEqual(res, 1)

    def test_1(self):
        nums = [4,1,2,1,2]
        res = self.sol.singleNumber(nums)
        print("result: {}".format(res))
        self.assertEqual(res, 4)
