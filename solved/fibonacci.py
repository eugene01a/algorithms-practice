from unittest import TestCase

import ddt

'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).


Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Note:

0 <= N <= 30.
'''


class Solution(object):

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """

        """
        :type N: int
        :rtype: int
        """
        cache={0:0, 1:1}
        def helper(N):
            if N in cache:
                return cache[N]
            else:
                cache[N] = helper(N - 1) + helper(N - 2)
            return cache[N]
        return helper(N)

@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([2], 1),
        ([3], 2),
        ([4], 3),
        ([5], 5),
        ([6], 8),
        ([7], 13),

    )
    def test_solution(self, args, output):
        response = self.solution.fib(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
