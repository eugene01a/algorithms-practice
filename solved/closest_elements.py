from unittest import TestCase

import ddt

'''
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements iwn the array and x will not exceed 104
UPDATE (2017/9/19):
The arr parameter had been changed to an array of integers (instead of a list of integers). Please reload the code definition to get the latest changes.
'''


class Solution(object):
    def findClosestElements(self, A, k, x):
        left, right = 0, len(A) - k
        while left < right:
            mid = (left + right) / 2
            if x - A[mid] > A[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return A[left:left + k]


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[0, 1, 1, 1, 2, 3, 6, 7, 8, 9], 9, 4], [0, 1, 1, 1, 2, 3, 6, 7, 8, ]),
        ([[1, 2, 3, 4, 5], 4, 3], [1, 2, 3, 4]),
        ([[1, 2], 1, 1], [1]),
        ([[1], 1, 1], [1]),
        ([[0, 0, 0, 1, 3, 5, 6, 7, 8, 8], 2, 2], [1, 3]),
        ([[1, 2, 5, 5, 6, 6, 7, 7, 8, 9], 7, 7], [5, 5, 6, 6, 7, 7, 8]),
        ([[0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5], [3, 3, 4]),
        ([[1, 1, 2, 3, 3, 3, 4, 6, 8, 8], 6, 1], [1, 1, 2, 3, 3, 3])
    )
    def test_solution(self, args, output):
        response = self.solution.findClosestElements(*args)
        self.assertEqual(response, output, "expected: {} \n actual: {}\n".format(output, response))
