"""
Contains Duplicate
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
from unittest import TestCase


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False


class TestSolution(TestCase):
    sol = Solution()

    def test_0(self):
        nums = [1, 2, 3, 4]
        res = self.sol.containsDuplicate(nums)
        print("result: {}".format(res))
        self.assertFalse(res)

    def test_1(self):
        nums = [1,2,3,1]
        res = self.sol.containsDuplicate(nums)
        print("result: {}".format(res))
        self.assertTrue(res)

    def test_3(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        res = self.sol.containsDuplicate(nums)
        print("result: {}".format(res))
        self.assertTrue(res)
