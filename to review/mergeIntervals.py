'''
PROBLEM
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

'''

from unittest import TestCase
from nose.plugins.attrib import attr
import ddt

class Solution(object):
    def mergeIntervals(self, intervals):
        intervals.sort()
        i = 0
        while i < len(intervals) - 1:
            n1 = intervals[i]
            n2 = intervals[i + 1]
            if n2[0] <= n1[1]:
                if n2[1] > n1[1]:
                    intervals[i] = [n1[0], n2[1]]
                intervals.pop(i + 1)
            else:
                i += 1
        return intervals


@ddt.ddt
@attr("Sort", "Merge")
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[[1, 4], [4, 5]]], [[1, 5]]),
        ([[[1, 4], [0, 4]]], [[0, 4]]),
        ([[[1, 3], [2, 6], [8, 10], [15, 18]]], [[1, 6], [8, 10], [15, 18]]),
    )
    def test_solution(self, args, output):
        response = self.solution.mergeIntervals(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
