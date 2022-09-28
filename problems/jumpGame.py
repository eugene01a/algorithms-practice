'''

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

'''


from unittest import TestCase
import ddt
from nose.plugins.attrib import attr

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        https://medium.com/algorithms-and-leetcode/greedy-algorithm-explained-using-leetcode-problems-80d6fee071c4

        """
        print("nums={}".format(nums))
        if not nums:
            return True
        maxReachableDistance = 0
        tab=''
        print("maxReachableDistance={}".format(maxReachableDistance))
        for i in range(len(nums)):
            if i > maxReachableDistance: #means we cant get to current position
                break
            maxReachableDistance = max(maxReachableDistance, i+nums[i])
            print("{}i={} ({}), maxReachableDistance={}".format(tab+'\t', i, nums[i], maxReachableDistance))
        return maxReachableDistance >= len(nums)-1


@ddt.ddt
@attr("Greedy")
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[2,3,1,1,4]], True),
        ([[3,2,1,0,4]], False),
        )
    def test_solution(self, args, output):
        response = self.solution.canJump(*args)
        self.assertEqual(output, response, "\n\nexpected: {} \n actual: {}\n".format(output, response))
