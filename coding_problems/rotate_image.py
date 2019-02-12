"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""
import unittest
import math


class Solution:
    def rotate(self, matrix):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for first in range(len(matrix) // 2):
            last = len(matrix) - 1 - first
            j = 0
            # for j in range(len(matrix) - i * 2):
            while j < math.ceil(len(matrix) / 2):
                tmp = matrix[first][first + j]

                matrix[first][first + j] = matrix[last - j][first]
                matrix[last - j][first] = matrix[last][last - j]
                matrix[last][last - j] = matrix[first + j][last]
                matrix[first + j][last] = tmp
                #
                # matrix[first + j][last], matrix[last][last - j], matrix[last - j][first], matrix[first][first + j] = \
                #     matrix[first][first + j], matrix[first + j][last], matrix[last][last - j], matrix[last - j][first]
                j += 1
        return matrix


class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_0(self):
        matrix = \
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
        import copy
        orig = copy.deepcopy(matrix)
        self.sol.rotate(matrix)
        print("result: {}".format(matrix))
        for i in range(len(matrix)):
            print("{}\t{}".format(orig[i], matrix[i]))
        self.assertEqual(
            [
                [7, 4, 1],
                [8, 5, 2],
                [9, 6, 3]
            ]
            , matrix)

    def test_1(self):
        matrix = \
            [
                [5, 1, 9, 11],
                [2, 4, 8, 10],
                [13, 3, 6, 7],
                [15, 14, 12, 16]
            ]
        self.sol.rotate(matrix)
        print("result: {}".format(matrix))
        self.assertEqual(
            [
                [15, 13, 2, 5],
                [14, 3, 4, 1],
                [12, 6, 8, 9],
                [16, 7, 10, 11]
            ]
            , matrix)

    def test_2(self):
        matrix = \
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]
            ]
        import copy
        orig = copy.deepcopy(matrix)
        self.sol.rotate(matrix)
        print("result: {}".format(matrix))
        for i in range(len(matrix)):
            print("{}\t\t{}".format(orig[i], matrix[i]))
        self.assertEqual(
            [
                [13, 9, 5, 1],
                [14, 10, 6, 2],
                [15, 11, 7, 3],
                [16, 12, 8, 4]
            ]
            , matrix)


if __name__ == '__main__':
    unittest.main()
