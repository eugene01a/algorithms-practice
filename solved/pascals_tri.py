from unittest import TestCase

import ddt

'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        recursive relation
        sol[i][j] = sol[i-1][j-1]+sol[i-1][j]
        where j<=i, i<=numRows

        base case:
        sol[i][j]=1

        """
        sol = []

        def add_num(row, col):
            if col == row:
                sol[row].append(1)
            elif col==0:
                sol[row].append(1)
                add_num(row, col + 1)
            else:
                sol[row].append(sol[row - 1][col - 1] + sol[row - 1][col])
                add_num(row, col + 1)

        for i in range(numRows):
            sol.append([])
            add_num(i,0)
        return sol


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([5], [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
         ), )
    def test_solution(self, args, output):
        response = self.solution.generate(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
