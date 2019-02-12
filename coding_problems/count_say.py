"""
Implement countAndSay().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr()
and Java's indexOf().
"""
import unittest


class Solution(object):
    # not my solution dont know what you want from me :)
    def countAndSay(self, n):
        if n == 1:
            return "1"
        if n == 2:
            return "11"

        def countSay(string):
            res, count = "", 1
            for i in range(1, len(string)):
                if string[i - 1] == string[i]:
                    count += 1
                else:
                    res += str(count) + string[i - 1]
                    count = 1
                if i == len(string) - 1:
                    res += str(count) + string[i]
            return res

        dp = [""] * (n + 1)
        dp[1], dp[2] = "1", "11"
        for i in range(3, n + 1):
            dp[i] = countSay(dp[i - 1])
        return dp[n]


class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_0(self):
        res = self.sol.countAndSay(1)
        self.assertEqual("1", res)

    def test_1(self):
        res = self.sol.countAndSay(4)
        self.assertEqual("1211", res)


if __name__ == '__main__':
    unittest.main()
