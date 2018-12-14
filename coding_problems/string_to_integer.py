"""
8. String to Integer (atoi)
Medium
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as
possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no
effect on the behavior of this function. If the first sequence of non-whitespace characters in str is not a valid
integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters,
no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
Example 1:

Input: "42"
Output: 42

Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Therefore INT_MIN (-231) is returned.
"""
import unittest


class Solution:
    def myAtoi(self, in_str):
        """
        :type in_str: str
        :rtype: int
        """
        sign = 1
        in_str = in_str.strip(' ')
        for idx, val in enumerate(in_str):
            if idx > 0:
                if '0' <= in_str[idx - 1] <= '9' and (val == '-' or val == '+'):
                    in_str = in_str[:idx]
                    break
                if (in_str[idx - 1] == '+' and val == '-') or \
                        (in_str[idx - 1] == '-' and val == '+') or \
                        (in_str[idx - 1] == '-' and val == '-') or \
                        (in_str[idx - 1] == '+' and val == '+'):
                    return 0
            if '0' <= val <= '9':
                if idx > 0:
                    if in_str[idx - 1] == '-':
                        sign = -1
                        in_str = in_str[idx:]
                        break
                    if in_str[idx - 1] == '+':
                        in_str = in_str[idx:]
                        break

        if len(in_str) > 0 and ord('0') <= ord(in_str[0]) <= ord('9'):
            rv = 0
            for s in in_str:
                if ord('0') <= ord(s) <= ord('9'):
                    rv *= 10
                    rv = rv + ord(s) - 48
                else:
                    break
            rv = rv * sign
            if rv < -2 ** 31:
                return -2 ** 31
            if 2 ** 31 - 1 < rv:
                return 2 ** 31 - 1
            return rv
        return 0


class TestSolution(unittest.TestCase):
    solution = Solution()
    myAtoi = solution.myAtoi

    def test_positive(self):
        self.assertEqual(42, self.solution.myAtoi('42'))
        self.assertEqual(self.myAtoi("123-"), 123)

    def test_negative(self):
        self.assertEqual(self.myAtoi("-42"), -42)

    def test_string_after_number(self):
        self.assertEqual(self.myAtoi("4193 with words"), 4193)

    def test_string_before_number(self):
        self.assertEqual(self.myAtoi("words and 987"), 0)

    def test_negative_out_of_range_32_bit(self):
        self.assertEqual(self.myAtoi("-91283472332"), -2147483648)

    def test_empty(self):
        self.assertEqual(self.myAtoi(""), 0)

    def test_negatives(self):
        self.assertEqual(self.myAtoi("-"), 0)
        self.assertEqual(self.myAtoi("--"), 0)

    def test_two_signs(self):
        self.assertEqual(self.myAtoi("+-2"), 0)
        self.assertEqual(self.myAtoi("-13+8"), -13)
        self.assertEqual(self.myAtoi("++8"), 0)
        self.assertEqual(self.myAtoi("--8"), 0)

    def test_explicit_positive(self):
        self.assertEqual(self.myAtoi("+1"), 1)

    def test_spaces(self):
        self.assertEqual(self.myAtoi("  0000000000012345678"), 12345678)

    def test_expression(self):
        self.assertEqual(self.myAtoi("0-1"), 0)


if __name__ == '__main__':
    unittest.main()
    # sol = Solution()
    # res = sol.myAtoi("4193 with words")
    # print(res)
