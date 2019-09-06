from unittest import TestCase

import ddt

'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
'''

from collections import deque


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        rows = len(matrix)
        cols = len(matrix[0])
        queue = deque()
        visited = set()
        sol = list(matrix)

        for i in range(rows):
            for j in range(cols):
                visited.clear()
                queue.append((matrix[i][j], (i, j)))
                while queue:
                    val, (r, c) = queue.popleft()
                    if val == 0:
                        dist = abs(r - i) + abs(c - j)
                        sol[i][j] = dist
                        queue.clear()
                    else:
                        if r > 0:
                            n = (r - 1, c)
                            if n not in visited:
                                queue.append((matrix[r - 1][c], n))
                                visited.add(n)
                        if r < rows - 1:
                            n = (r + 1, c)
                            if n not in visited:
                                queue.append((matrix[r + 1][c], n))
                                visited.add(n)
                        if c > 0:
                            n = (r, c - 1)
                            if n not in visited:
                                queue.append((matrix[r][c - 1], n))
                                visited.add(n)
                        if c < cols - 1:
                            n = (r, c + 1)
                            if n not in visited:
                                queue.append((matrix[r][c + 1], n))
                                visited.add(n)
        return sol


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[[0, 0, 0],
           [0, 1, 0],
           [1, 1, 1]]], [[0, 0, 0],
                         [0, 1, 0],
                         [1, 2, 1]]),
        ([[[0, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]], [[0, 0, 0],
                         [0, 1, 0],
                         [0, 0, 0]]
         ),
    )
    def test_solution(self, args, output):
        response = self.solution.updateMatrix(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))


