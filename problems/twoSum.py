'''
Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

from unittest import TestCase
from nose.plugins.attrib import attr
import ddt

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        memo={}
        for i, n in enumerate(nums):
            m = target-n
            print "i={}, n={}, m={}, memo={}".format(i, n,m,memo)
            if m in memo:
                return [memo[m], i]
            else:
                memo[n]=i

@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[2, 7, 11, 15], 9], [0,1]),
    )
    @attr("two pointers")
    def test_solution(self, args, output):
        response = self.solution.twoSum(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
