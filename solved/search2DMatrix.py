from unittest import TestCase

import ddt

'''
PROBLEM
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        def bsRows(rows, target):

            left, right = 0, len(rows) - 1
            while left <= right:
                mid = (left + right) // 2
                if target > rows[mid][-1]:
                    left = mid + 1
                elif target < rows[mid][0]:
                    right = mid - 1
                else:
                    return bsCols(rows[mid], target)

            return False

        def bsCols(cols, target):

            left, right = 0, len(cols) - 1
            while left <= right:
                mid = (left + right) // 2
                if cols[mid] == target:
                    return True
                elif cols[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return False

        return bsRows(matrix, target)


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3], True),
        ([[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 13], False),
        ([[[]], 0], False),
        ([[], 0], False),
        ([[[1]], 1], True),
        ([[[1], [3]], 3], True)
    )
    def test_solution(self, args, output):
        response = self.solution.searchMatrix(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
