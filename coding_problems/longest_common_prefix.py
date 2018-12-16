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
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        min_word_len = min(len(x) for x in strs)
        res = 0
        for i in range(min_word_len):
            for s in strs[:-1]:
                if s[i] != strs[-1][i]:
                    if i == min_word_len:
                        i += 1
                    return strs[0][:i]
            res += 1
        return strs[0][:res]


class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_0(self):
        res = self.sol.longestCommonPrefix(["flower", "flow", "flight"])
        print("result: {}".format(res))
        self.assertEqual('fl', res)

    def test_1(self):
        res = self.sol.longestCommonPrefix(["dog", "racecar", "car"])
        print("result: {}".format(res))
        self.assertEqual('', res)

    def test_2(self):
        res = self.sol.longestCommonPrefix(["dog", "dog", "dog"])
        print("result: {}".format(res))
        self.assertEqual('dog', res)

    def test_3(self):
        res = self.sol.longestCommonPrefix([])
        print("result: {}".format(res))
        self.assertEqual('', res)

    def test_4(self):
        res = self.sol.longestCommonPrefix(["aa", "a"])
        print("result: {}".format(res))
        self.assertEqual('a', res)

    def test_5(self):
        res = self.sol.longestCommonPrefix(["a"])
        print("result: {}".format(res))
        self.assertEqual('a', res)

    def test_6(self):
        res = self.sol.longestCommonPrefix(["c","c"])
        print("result: {}".format(res))
        self.assertEqual('c', res)


if __name__ == '__main__':
    unittest.main()
