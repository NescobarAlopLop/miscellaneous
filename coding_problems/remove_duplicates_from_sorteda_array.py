"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
Internally you can think of this:
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

import unittest


class Solution:

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        rv = 0
        for current in range(len(nums)):
            if nums[rv] < nums[current]:
                rv += 1
                nums[rv], nums[current] = nums[current], nums[rv]
        return rv + 1


class TestSolution(unittest.TestCase):

    def test_arrays1(self):
        sol = Solution()
        nums = [1,1,2]
        res = sol.removeDuplicates(nums)
        print("result: {}".format(nums[:res]))
        self.assertEqual(2, res)

    def test_arrays2(self):
        sol = Solution()
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        res = sol.removeDuplicates(nums)
        print("result: {}".format(nums[:res]))
        self.assertEqual(5, res)

    def test_empty(self):
        sol = Solution()
        nums = []
        res = sol.removeDuplicates(nums)
        print("result: {}".format(nums[:res]))
        self.assertEqual(0, res)

    def test_no_duplicates(self):
        sol = Solution()
        nums = [1, 2, 3]
        res = sol.removeDuplicates(nums)
        print("result: {}".format(nums[:res]))
        self.assertEqual(3, res)


if __name__ == '__main__':
    unittest.main()
