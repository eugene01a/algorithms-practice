from unittest import TestCase

import ddt

'''
PROBLEM
'''


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        sol = triangle[-1]

        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                sol[j] = min(sol[j], sol[j+1])+triangle[i][j]

        return sol[0]

@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[[-7],
           [-2,1],
           [-5,-5,9],
           [-4,-5,4,4],
           [-6,-6,2,-1,-5],
           [3,7,8,-3,7,-9],
           [-9,-1,-9,6,9,0,7],
           [-7,0,-6,-8,7,1,-4,9],
           [-3,2,-6,-9,-7,-6,-9,4,0],
           [-8,-6,-3,-9,-2,-6,7,-5,0,7],
           [-9,-1,-2,4,-2,4,4,-1,2,-5,5],
           [1,1,-6,1,-2,-4,4,-2,6,-6,0,6],
           [-3,-3,-6,-2,-6,-2,7,-9,-5,-7,-5,5,1]]], -63))


    def test_solution(self, args, output):
        response = self.solution.minimumTotal(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
