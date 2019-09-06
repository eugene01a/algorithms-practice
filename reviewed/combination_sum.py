'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

'''
from unittest import TestCase

import ddt
from nose.plugins.attrib import attr


class Solution(object):
    def combinationSum(self, candidates, target):
        sol = []
        length = len(candidates)

        def backtrack(start, tmp, target):
            if target == 0:
                sol.append(tmp)
                return
            for i in range(start, length):
                num = candidates[i]
                if num > target:
                    continue
                backtrack(i, tmp + [num], target - num)

        backtrack(0, [], target)
        return sol


@ddt.ddt
@attr("backtracking")
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[2, 3, 6, 7], 7], [[2, 2, 3], [7]]),
        ([[2, 3, 5], 8], [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    )
    def test_solution(self, args, output):
        response = self.solution.combinationSum(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
