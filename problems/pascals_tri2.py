from unittest import TestCase

import ddt

'''
Given a non-negative index k where k <= 33, return the kth index row of the Pascal's
triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 3
Output: [1,3,3,1]
Follow up:
Could you optimize your algorithm to use only O(k) extra space?
'''


class Solution(object):
    count = 1

    def getRow(self, rowIndex):
        cache={}
        def helper(i, j):
            if cache.get((i,j), {}):
                return cache[(i,j)]
            elif j == 1 or i == j:
                return 1
            elif j == 2 or j == i - 1:
                return i - 1
            else:
                right= helper(i - 1, j)
                left=helper(i - 1, j - 1)
                cache[(i,j)]=right+left
                return right+left

        sol = [1]*(rowIndex+1)
        for colIndex in range(rowIndex + 1):
            sol[colIndex]=helper(rowIndex + 1, colIndex + 1)
        print self.count
        return sol


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([9], [1,9,36,84,126,126,84,36,9,1]), )
    def test_solution(self, args, output):
        response = self.solution.getRow(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
