'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

from unittest import TestCase

import ddt


class Solution(object):
    def correct_fourSum(self, nums, target):
        nums.sort()
        ans = []
        for a in range(len(nums) - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, len(nums) - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                c, d = b + 1, len(nums) - 1
                while c < d:
                    tot = nums[a] + nums[b] + nums[c] + nums[d]
                    if tot == target:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])
                    if tot <= target:
                        c += 1
                        while nums[c] == nums[c - 1] and c < d:
                            c += 1
                    if tot >= target:
                        d -= 1
                        while nums[d] == nums[d + 1] and c < d:
                            d -= 1
        return ans

    def my_fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []

        sol = set()
        nums.sort()
        for a in range(len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):
                c, d = b + 1, len(nums) - 1
                while c < d:
                    s = (nums[a], nums[b], nums[c], nums[d])
                    tot = sum(s)
                    if tot == target:
                        sol.add(s)
                        c+=1
                        d-=1
                    elif tot < target:
                        c += 1
                    else:
                        d -= 1

        return [list(t) for t in sol]


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[-3, -1, 0, 2, 4, 5], 2], [[-3, -1, 2, 4]]),
        ([[1, 0, -1, 0, -2, 2], 0], [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
    )
    def test_solution(self, args, output):
        response = self.solution.my_fourSum(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
