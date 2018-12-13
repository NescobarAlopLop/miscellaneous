"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
import unittest


class Solution:
    @staticmethod
    def permutation(s1, s2):
        if len(s1) != len(s2):
            return False
        char_counter = [0] * 256  # assumption
        for c in s1:
            char_counter[ord(c)] += 1
        for c in s2:
            char_counter[ord(c)] -= 1
        for c in char_counter:
            if c != 0:
                return False
        return True

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # s = sorted(s)
        # t = sorted(t)
        # return s == t
        return self.permutation(s, t)


class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_0(self):
        s = "anagram"
        t = "nagaram"
        res = self.sol.isAnagram(s, t)
        print("result: {}".format(res))
        self.assertTrue(res)

    def test_1(self):
        s = "rat"
        t = "car"
        res = self.sol.isAnagram(s, t)
        print("result: {}".format(res))
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()
