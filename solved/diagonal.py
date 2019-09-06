from unittest import TestCase

import ddt

'''
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

(0,0)
(0,1)
(1,0)
(2,0)
(1,1)
(0,2)
(1,2)
(2,1)
(2,2)

Output:  [1,2,4,7,5,3,6,8,9]


Explanation:
Note:

The total number of elements of the given matrix will not exceed 10,000.

'''


class Solution(object):

    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        r, c = 0, 0
        up = True
        sol = [1] * m * n

        def next_rc(r, c, up):
            if up:
                if r > 0 and c < n - 1:
                    return r - 1, c + 1, True
                if r == 0 and c != n - 1:
                    return r, c + 1, False
                if c == n - 1:
                    return r + 1, c, False
            else:
                if r < m - 1 and c > 0:
                    return r + 1, c - 1, False
                if r != m - 1 and c == 0:
                    return r+1, c, True
                if r == m - 1:
                    return r, c+1, True

        for i in range(len(sol)):
            sol[i] = matrix[r][c]
            r, c, up = next_rc(r, c, up)

        return sol


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([
             [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
         ],
         [1, 2, 4, 7, 5, 3, 6, 8, 9]
        ),
        ([
             [[2, 5],
              [8, 4],
              [0, -1]]
         ],
         [2, 5, 8, 0, 4, -1]
        ),
        ([
             [[2, 5, 8],
              [8, 4, -1]]
         ],
         [2, 5, 8, 4, 8, -1]
        ),
        ([
             []
         ],
         []
        ),
        ([
             [[1]]
         ],
         [1]),
        ([
             [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
         ],
         [1, 2, 5, 9, 6, 3, 4, 7, 10, 13, 14, 11, 8, 12, 15, 16]),
        ([
             [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]]

         ],
         [1, 2, 6, 11, 7, 3, 4, 8, 12, 16, 21, 17, 13, 9, 5, 10, 14, 18, 22, 23, 19, 15, 20, 24, 25]
        )
    )
    def test_solution(self, args, output):
        response = self.solution.findDiagonalOrder(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
