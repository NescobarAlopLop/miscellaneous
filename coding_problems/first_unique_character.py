"""
 Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
"""
import unittest


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1


class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_0(self):
        s = "leetcode"
        res = self.sol.firstUniqChar(s)
        print("result: {}".format(res))
        self.assertEqual(res, 0)

    def test_1(self):
        s = "loveleetcode"
        res = self.sol.firstUniqChar(s)
        print("result: {}".format(res))
        self.assertEqual(res, 2)


if __name__ == '__main__':
    unittest.main()
