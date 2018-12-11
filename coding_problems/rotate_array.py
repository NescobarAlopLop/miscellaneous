"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:

    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?
"""
from unittest import TestCase


class Solution:

    def reverse(self, nums, start, end):
        while start < end and start < len(nums) - 1 and end > 0:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start += 1
            end -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)


class TestSolution(TestCase):
    sol = Solution()

    def test_0(self):
        nums = [1, 2]
        self.sol.rotate(nums, 0)
        print("result: {}".format(nums))
        self.assertEqual([1, 2], nums)

    def test_1(self):
        nums = [1, 2, 3]
        self.sol.rotate(nums, 1)
        print("result: {}".format(nums))
        self.assertEqual([3, 1, 2], nums)

    def test_2(self):
        nums = [1, 2, 3, 4]
        self.sol.rotate(nums, 2)
        print("result: {}".format(nums))
        self.assertEqual([3, 4, 1, 2], nums)

    def test_3(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        self.sol.rotate(nums, 3)
        print("result: {}".format(nums))
        self.assertEqual([5, 6, 7, 1, 2, 3, 4], nums)

    def test_4(self):
        nums = [-1, -100, 3, 99]
        self.sol.rotate(nums, 2)
        print("result: {}".format(nums))
        self.assertEqual([3, 99, -1, -100], nums)

    def test_5(self):
        nums = [-1]
        self.sol.rotate(nums, 2)
        print("result: {}".format(nums))
        self.assertEqual([-1], nums)

    def test_6(self):
        nums = [1, 2]
        self.sol.rotate(nums, 3)
        print("result: {}".format(nums))
        self.assertEqual([2, 1], nums)
