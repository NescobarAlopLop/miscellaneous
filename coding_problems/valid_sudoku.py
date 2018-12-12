"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Example 2:
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Note:
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
    The given board contain only digits 1-9 and the character '.'.
    The given board size is always 9x9.
"""
import unittest


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return \
            self.check_rows(board) and \
            self.check_cols(board) and \
            self.check_cubes(board)

    def check_rows(self, board):
        for row in board:
            if not self.is_row_valid(row):
                return False
        return True

    def check_cols(self, board):
        for col in range(9):
            if not self.is_col_valid(board, col):
                return False
        return True

    def check_cubes(self, board):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.is_quad_valid(board, i, j):
                    return False
        return True

    @staticmethod
    def is_row_valid(row):
        seen = set()
        for val in row:
            if val in seen:
                return False
            if val != '.':
                seen.add(val)
        return True

    @staticmethod
    def is_col_valid(board, col_idx):
        seen = set()
        for r in range(9):
            if board[r][col_idx] in seen:
                return False
            if board[r][col_idx] != '.':
                seen.add(board[r][col_idx])
        return True

    @staticmethod
    def is_quad_valid(board, start_row, start_col):
        seen = set()
        for r in range(start_row, start_row + 3, 1):
            for c in range(start_col, start_col + 3, 1):
                if board[r][c] in seen:
                    return False
                if board[r][c] != '.':
                    seen.add(board[r][c])
        return True


class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_valid_row(self):
        board = [
                    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
                ]
        res = self.sol.isValidSudoku(board)
        print("result: {}".format(res))
        self.assertTrue(res)

    def test_invalid_row(self):
        board = [
                    ["5", "3", ".", ".", "7", ".", "7", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
                ]
        res = self.sol.isValidSudoku(board)
        print("result: {}".format(res))
        self.assertFalse(res)

    def test_invalid_col(self):
        board = [
                    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", "8", ".", "8", ".", ".", "7", "9"]
                ]
        res = self.sol.isValidSudoku(board)
        print("result: {}".format(res))
        self.assertFalse(res)

    def test_invalid_sudoku(self):
        board = [
                    ["8","3",".",".","7",".",".",".","."],
                    ["6",".",".","1","9","5",".",".","."],
                    [".","9","8",".",".",".",".","6","."],
                    ["8",".",".",".","6",".",".",".","3"],
                    ["4",".",".","8",".","3",".",".","1"],
                    ["7",".",".",".","2",".",".",".","6"],
                    [".","6",".",".",".",".","2","8","."],
                    [".",".",".","4","1","9",".",".","5"],
                    [".",".",".",".","8",".",".","7","9"]
                ]
        res = self.sol.isValidSudoku(board)
        print("result: {}".format(res))
        self.assertFalse(res)

    def test_invalid_sudoku_1(self):
        board = [
                    [".", ".", "4", ".", ".", ".", "6", "3", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", "."],
                    ["5", ".", ".", ".", ".", ".", ".", "9", "."],
                    [".", ".", ".", "5", "6", ".", ".", ".", "."],
                    ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
                    [".", ".", ".", "7", ".", ".", ".", ".", "."],
                    [".", ".", ".", "5", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", "."]
                ]
        res = self.sol.isValidSudoku(board)
        print("result: {}".format(res))
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()
