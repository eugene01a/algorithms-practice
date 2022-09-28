from unittest import TestCase

import ddt

'''
PROBLEM
'''


class Solution(object):
    def generateMatrix(self, n):
        A, lo = [], n * n + 1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [range(lo, hi)] + [list(x) for x in zip(*A[::-1])]
        return A


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([3], [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]]))
    def test_solution(self, args, output):
        response = self.solution.generateMatrix(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
