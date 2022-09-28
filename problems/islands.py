from unittest import TestCase

import ddt

'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''


class Solution(object):
    def noIslands(self, m):

        sol = 0
        queue = []
        visited=set()
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] ==1 and (i,j) not in visited:
                    sol+=1
                    visited.add((i,j))
                    queue.append((i,j))
                    while queue:
                        (r,c)=queue.pop(0)
                        if (r,c) not in visited and m[r][c]==1:
                            visited.add((i, j))
                            if c>0:
                                if m[r][c-1] ==1 and (r,c-1) not in visited:
                                    queue.append((r,c-1))
                            if c<len(m[0])-1:
                                if m[r][c-1] ==1 and (r,c+1) not in visited:
                                    queue.append((r,c+1))
                            if c>0:
                                if m[r-1][c] ==1 and (r-1,c) not in visited:
                                    queue.append((r-1,c))
                            if c>0:
                                if m[r+1][c] ==1 and (r+1,c) not in visited:
                                    queue.append((r+1,c))




        return sol


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(([[[1, 1, 1, 1, 0],
                 [1, 1, 0, 1, 0],
                 [1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0]]], 1),
              ([[[1, 1, 0, 0, 0],
                 [1, 1, 0, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 1]]], 3))
    def test_solution(self, args, output):
        response = self.solution.noIslands(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
