from unittest import TestCase

import ddt

'''
Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321
'''


class Solution(object):

    def plusOne(self, digits):
        digits[-1] += 1
        for idx in range(1, len(digits)):
            if digits[-idx] == 10:
                digits[-idx] = 0
                digits[-(idx + 1)] += 1
            else:
                return digits
        if digits[0] == 10:
            digits = [1, 0] + digits[1:]

        return digits


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[1, 2, 3]], [1, 2, 4]),
        ([[4, 3, 2, 1]], [4, 3, 2, 2]),
        ([[1, 0, 9]], [1, 1, 0]),
        ([[1, 9, 9]], [2, 0, 0]),
        ([[9, 9]], [1, 0, 0]),
    )
    def test_solution(self, args, output):
        response = self.solution.plusOne(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
