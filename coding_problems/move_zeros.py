"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
"""
from unittest import TestCase


class Solution:
    @staticmethod
    def get_next(nums, start, zero=True):
        for idx in range(start, len(nums)):
            if zero and nums[idx] == 0:
                return idx
            if not zero and nums[idx] != zero:
                return idx
        return len(nums)

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        z = self.get_next(nums, 0, zero=True)
        n = self.get_next(nums, 0, zero=False)

        while n < len(nums):
            if n > z and nums[n] != 0:
                nums[z], nums[n] = nums[n], nums[z]
                z = self.get_next(nums, z, zero=True)
                n = self.get_next(nums, n, zero=False)
                continue
            else:
                n += 1

class TestSolution(TestCase):
    sol = Solution()

    def test_0(self):
        nums = [0, 1, 2, 3, 4]
        self.sol.moveZeroes(nums)
        print("result: {}".format(nums))
        self.assertEqual([1, 2, 3, 4, 0], nums)

    def test_1(self):
        nums = [0, 1, 0, 2, 0, 3, 0, 1]
        self.sol.moveZeroes(nums)
        print("result: {}".format(nums))
        self.assertEqual([1, 2, 3, 1, 0, 0, 0, 0], nums)

    def test_3(self):
        nums = [0,1,0,3,12]
        self.sol.moveZeroes(nums)
        print("result: {}".format(nums))
        self.assertEqual([1, 3, 12, 0, 0], nums)

    def test_4(self):
        nums = [1]
        self.sol.moveZeroes(nums)
        print("result: {}".format(nums))
        self.assertEqual([1], nums)

    def test_5(self):
        nums = [1, -2, 0, 0, 3, 0, 4, 0]
        self.sol.moveZeroes(nums)
        print("result: {}".format(nums))
        self.assertEqual([1, -2, 3, 4, 0, 0, 0, 0], nums)

    def test_6(self):
        nums = [-959151711,623836953,209446690,-1950418142,1339915067,-733626417,481171539,-2125997010,-1225423476,1462109565,147434687,-1800073781,-1431212205,-450443973,50097298,753533734,-747189404,-2070885638,0,-1484353894,-340296594,-2133744570,619639811,-1626162038,669689561,0,112220218,502447212,-787793179,0,-726846372,-1611013491,204107194,1605165582,-566891128,2082852116,0,532995238,-1502590712,0,2136989777,-2031153343,371398938,-1907397429,342796391,609166045,-2007448660,-1096076344,-323570318,0,-2082980371,2129956379,-243553361,-1549960929,1502383415,0,-1394618779,694799815,78595689,-1439173023,-1416578800,685225786,-333502212,-1181308536,-380569313,772035354,0,-915266376,663709718,1443496021,-777017729,-883300731,-387828385,1907473488,-725483724,-972961871,-1255712537,383120918,1383877998,1722751914,0,-1156050682,1952527902,-560244497,1304305692,1173974542,-1313227247,-201476579,-298899493,-1828496581,-1724396350,1933643204,1531804925,1728655262,-955565449,0,-69843702,-461760848,268336768,1446130876]
        self.sol.moveZeroes(nums)
        print("result: {}".format(nums))
        self.assertEqual([-959151711,623836953,209446690,-1950418142,1339915067,-733626417,481171539,-2125997010,-1225423476,1462109565,147434687,-1800073781,-1431212205,-450443973,50097298,753533734,-747189404,-2070885638,-1484353894,-340296594,-2133744570,619639811,-1626162038,669689561,112220218,502447212,-787793179,-726846372,-1611013491,204107194,1605165582,-566891128,2082852116,532995238,-1502590712,2136989777,-2031153343,371398938,-1907397429,342796391,609166045,-2007448660,-1096076344,-323570318,-2082980371,2129956379,-243553361,-1549960929,1502383415,-1394618779,694799815,78595689,-1439173023,-1416578800,685225786,-333502212,-1181308536,-380569313,772035354,-915266376,663709718,1443496021,-777017729,-883300731,-387828385,1907473488,-725483724,-972961871,-1255712537,383120918,1383877998,1722751914,-1156050682,1952527902,-560244497,1304305692,1173974542,-1313227247,-201476579,-298899493,-1828496581,-1724396350,1933643204,1531804925,1728655262,-955565449,-69843702,-461760848,268336768,1446130876,0,0,0,0,0,0,0,0,0,0], nums)
