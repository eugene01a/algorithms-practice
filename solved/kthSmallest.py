from unittest import TestCase

import ddt

'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [1,  5,  9],   
   [6,  7,  9],
   [8, 15, 15]
],
k = 8,

return 13.
'''

from heapq import *
class Solution:

    def find_Kth_smallest(matrix, k):
        minHeap = []
        for i in range(min(k, len(matrix))):
            heappush(minHeap, (matrix[i][0], 0, matrix[i]))
        numberCount, number = 0, 0
        while minHeap:
            number, i, row = heappop(minHeap)
            numberCount += 1
            if numberCount == k:
                break
            if len(row) > i + 1:
                heappush(minHeap, (row[i + 1], i + 1, row))
        return number


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8], 13))
    def test_solution(self, args, output):
        response = self.solution.kthSmallest(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
