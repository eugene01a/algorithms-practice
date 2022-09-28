from unittest import TestCase

import ddt

'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


class Solution(object):
    def correct_threeSumClosest(self, nums, target):
        nums.sort()
        res = sum(nums[:3])
        for i in xrange(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = sum((nums[i], nums[l], nums[r]))
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:  # break early
                    return res
        return res

    def my_threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        diff = target
        sol = sum(nums[:3])
        for a in range(len(nums) - 2):
            b, c = a + 1, len(nums) - 1
            while b < c:
                s = nums[a] + nums[b] + nums[c]
                if abs(s - target) < diff:
                    diff = s - target
                    sol = s
                if s == target:
                    return target
                elif s < target:
                    b += 1
                else:
                    c -= 1


        return sol

@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[-1, 2, 1, -4], 1], 2),
    )
    def test_solution(self, args, output):
        response = self.solution.correct_threeSumClosest(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
