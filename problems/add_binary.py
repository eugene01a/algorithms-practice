from unittest import TestCase

import ddt

'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2
:

Input: a = "1010", b = "1011"
Output: "10101"
'''


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """



@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]], [1, 2, 4, 7, 5, 3, 6, 8, 9]),
    )
    def test_solution(self, args, output):
        response = self.solution.addBinary(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
