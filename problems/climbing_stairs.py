from unittest import TestCase

import ddt

'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {0: 0, 1: 1}
        def helper(n):
            if n in cache:
                return cache[n]
            else:
                cache[n]=helper(n-1)+helper(n-2)
                return cache[n]
        return helper(n+1)
@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([2], 2),
        ([3], 3),
        ([4], 5),
        ([6], 13),

    )
    def test_solution(self, args, output):
        response = self.solution.climbStairs(*args)
        self.assertEqual(response, output, "expected: {} \n actual: {}\n".format(output, response))


