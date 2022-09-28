'''

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

'''

from unittest import TestCase

import ddt
from nose.plugins.attrib import attr


class Solution(object):
    def reverse(self, x):
        result = 0
        symbol = 1

        if x < 0:
            symbol = -1
            x = -x

        while x:
            result = result * 10 + x % 10
            x /= 10

        return 0 if result > pow(2, 31) else result * symbol


@ddt.ddt
@attr("Math")
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        (["hit", "cog", ["hot", "dot", "dog", "log", "cog"]], 5),
        (["lost", "miss", ["most", "mist", "miss", "lost", "fist", "fish"]], 4),
    )
    def test_solution(self, args, output):
        response = self.solution.ladderLength(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
