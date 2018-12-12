"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
import unittest

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = {}
        for idx, val in enumerate(nums):
            res[target - val] = idx

        for idx, val in enumerate(nums):
            if val in res:
                if idx != res[val]:
                    return [idx, res[val]]


class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_0(self):
        nums = [2, 7, 11, 15]
        res = self.sol.twoSum(nums, 9)
        print("result: {}".format(res))
        self.assertEqual(res, [0, 1])

    def test_1(self):
        nums = [3,2,4]
        res = self.sol.twoSum(nums, 6)
        print("result: {}".format(res))
        self.assertEqual(res, [1, 2])


if __name__ == '__main__':
    unittest.main()
