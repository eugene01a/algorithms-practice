'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
from unittest import TestCase

import ddt


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sol = [[]]

        def backtrack(subset, next_nums):
            sol.append(subset)
            for j in range(len(next_nums)):
                backtrack(subset + [next_nums[j]], next_nums[j + 1:])

        for i in range(len(nums)):
            subset = [nums[i]]
            next_nums = nums[i + 1:]
            backtrack(subset, next_nums)
        return sol


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(([[1, 2, 3]],
               [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
               ))
    def test_solution(self, args, expected):
        response = self.solution.subsets(*args)
        self.assertEqual(response, expected, "\n\nexpected: {} \n actual: {}\n".format(expected, response))
