from typing import List
from unittest import TestCase


class Solution:
    def __init__(self):
        self.neighbours = [
            (-1, -1),
            ( 0, -1),
            ( 1, -1),
            (-1,  0),
            ( 1,  0),
            (-1,  1),
            ( 0,  1),
            ( 1,  1),
        ]

    def count_neighbours(
        self,
        board,
        x,
        y,
    ):
        number_of_neighbours = 0
        for d_x, d_y in self.neighbours:
            current_x, current_y = x + d_x, y + d_y
            if current_x < 0 or current_y < 0 or current_x >= len(board[y]) or current_y >= len(board):
                continue

            if board[current_y][current_x]:
                number_of_neighbours += 1

        return number_of_neighbours

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbours_count = [
            [0] * len(board[0])
            for _ in range(len(board))
        ]
        for x in range(0, len(board[0])):
            for y in range(0, len(board)):
                neighbours_count[y][x] = self.count_neighbours(
                    board=board,
                    x=x,
                    y=y,
                )

        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] and neighbours_count[y][x] < 2:
                    board[y][x] = 0
                if board[y][x] and 2 <= neighbours_count[y][x] <= 3:
                    board[y][x] = 1
                if board[y][x] and neighbours_count[y][x] > 3:
                    board[y][x] = 0
                if not board[y][x] and neighbours_count[y][x] == 3:
                    board[y][x] = 1

    def count_neighbours_save_space(
        self,
        board,
        x,
        y,
    ):
        number_of_neighbours = 0
        for d_x, d_y in self.neighbours:
            current_x, current_y = x + d_x, y + d_y
            if current_x < 0 or current_y < 0 or current_x >= len(board[y]) or current_y >= len(board):
                continue

            if int(board[current_y][current_x]):
                number_of_neighbours += 1

        return number_of_neighbours

    def gameOfLifeSaveSpace(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for x in range(0, len(board[0])):
            for y in range(0, len(board)):
                board[y][x] += self.count_neighbours_save_space(
                    board=board,
                    x=x,
                    y=y,
                ) / 10

        for y in range(len(board)):
            for x in range(len(board[y])):
                if int(board[y][x]) and int(board[y][x] * 10 % 10) < 2:
                    board[y][x] = 0
                if int(board[y][x]) and 2 <= int(board[y][x] * 10 % 10) <= 3:
                    board[y][x] = 1
                if int(board[y][x]) and int(board[y][x] * 10 % 10) > 3:
                    board[y][x] = 0
                if not int(board[y][x]) and int(board[y][x] * 10 % 10) == 3:
                    board[y][x] = 1
                else:
                    board[y][x] = int(board[y][x])


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_0(self):
        board = [
            [1, 1],
            [1, 0]
        ]
        self.solution.gameOfLife(
            board=board,
        )
        self.assertEqual(
            first=[
                [1, 1],
                [1, 1]
            ],
            second=board,
        )

    def test_1(self):
        board = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]
        ]
        self.solution.gameOfLife(
            board=board,
        )
        print("result: {}".format(board))
        self.assertEqual(
            first=[
                [0, 0, 0],
                [1, 0, 1],
                [0, 1, 1],
                [0, 1, 0],
            ],
            second=board,
        )

    def test_3(self):
        board = [
            [1, 1],
            [1, 0]
        ]
        self.solution.gameOfLifeSaveSpace(
            board=board,
        )
        self.assertEqual(
            first=[
                [1, 1],
                [1, 1]
            ],
            second=board,
        )

    def test_4(self):
        board = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]
        ]
        self.solution.gameOfLifeSaveSpace(
            board=board,
        )
        print("result: {}".format(board))
        self.assertEqual(
            first=[
                [0, 0, 0],
                [1, 0, 1],
                [0, 1, 1],
                [0, 1, 0],
            ],
            second=board,
        )
