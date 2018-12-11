"""
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
"""
import unittest


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        idx1 = 0
        idx2 = 0
        rv = []
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] == nums2[idx2]:
                rv.append(nums1[idx1])
                idx1 += 1
                idx2 += 1
            elif nums1[idx1] < nums2[idx2]:
                idx1 += 1
            else:
                idx2 += 1
        return rv


class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_0(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        res = self.sol.intersect(nums1, nums2)
        print("result: {}".format(res))
        self.assertEqual([2, 2], res)

    def test_1(self):
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        res = self.sol.intersect(nums1, nums2)
        print("result: {}".format(res))
        self.assertEqual([4, 9], res)


if __name__ == '__main__':
    unittest.main()
