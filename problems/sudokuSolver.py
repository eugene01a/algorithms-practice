from collections import defaultdict
from unittest import TestCase

import ddt

'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.

'''


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        self.board = board
        self.rowMap = defaultdict(lambda: set([]))
        self.colMap = defaultdict(lambda: set([]))
        self.boxMap = defaultdict(lambda: set([]))

        def next_cell():
            for i in range(9):
                for j in range(9):
                    if self.board[i][j] == '.':
                        return (i, j)
            return (-1, -1)

        def assign_box(i, j):
            if 0 <= i < 3:
                if 0 <= j < 3:
                    box = 1
                elif 3 <= j < 6:
                    box = 2
                else:
                    box = 3
            elif 3 <= i < 6:
                if 0 <= j < 3:
                    box = 4
                elif 3 <= j < 6:
                    box = 5
                else:
                    box = 6
            else:
                if 0 <= j < 3:
                    box = 7
                elif 3 <= j < 6:
                    box = 8
                else:
                    box = 9
            return box

        def val_remove(i, j, c):
            self.board[i][j] = '.'
            self.rowMap[i].remove(c)
            self.colMap[j].remove(c)
            self.boxMap[assign_box(i, j)].remove(c)

        def val_add(i, j, c):
            self.board[i][j] = c
            self.rowMap[i].add(c)
            self.colMap[j].add(c)
            self.boxMap[assign_box(i, j)].add(self.board[i][j])

        def is_valid(i, j, c):
            if (c in self.colMap[j] or
                    c in self.rowMap[i] or
                    c in self.boxMap[assign_box(i, j)]):
                return False
            else:
                return True

        def backtrack():

            (i, j) = next_cell()
            if (i, j) == (-1, -1):
                return True
            for c in [str(num) for num in range(1, 10)]:
                if is_valid(i, j, c):
                    val_add(i, j, c)
                    if backtrack():
                        return True
                    val_remove(i, j, c)
                else:
                    continue
            return False

        for i in range(9):
            for j in range(9):
                if self.board[i][j] != '.':
                    val_add(i, j, self.board[i][j])
        backtrack()
        return self.board


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([
             [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
              [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
              ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
              [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
              [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
         ], [["5", "3", "4", "6", "7", "8", "9", "1", "2"], ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
             ["1", "9", "8", "3", "4", "2", "5", "6", "7"], ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
             ["4", "2", "6", "8", "5", "3", "7", "9", "1"], ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
             ["9", "6", "1", "5", "3", "7", "2", "8", "4"], ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
             ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]),

    )
    def test_solution(self, args, output):
        response = self.solution.solveSudoku(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
