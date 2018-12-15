"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
"""
import unittest


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        check_chars = []
        res = 0
        l = min(len(x) for x in strs)
        for i in range(l):
            for s in strs:
                check_chars.append(s[i])
            for c in range(len(check_chars)-1):
                if check_chars[c] != check_chars[-1]:
                    return strs[0][:i + 1]
                res += 1
        return strs[0][:res]

class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_0(self):
        res = self.sol.longestCommonPrefix(["flower","flow","flight"])
        print("result: {}".format(res))
        self.assertEqual(res, 'fl')

    def test_1(self):
        res = self.sol.longestCommonPrefix(["dog","racecar","car"])
        print("result: {}".format(res))
        self.assertEqual(res, '')

    def test_2(self):
        res = self.sol.longestCommonPrefix(["dog","dog","dog"])
        print("result: {}".format(res))
        self.assertEqual(res, '')


if __name__ == '__main__':
    unittest.main()
