from unittest import TestCase

import ddt

'''
Single Number
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hm = {}

        for num in nums:
            hm[num] = hm.get(num,0)+1
        for k, v in hm.items():
            if v == 1:
                return k


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[2, 2, 1]], 1),
        ([[4, 1, 2, 1, 2]], 4),

    )
    def test_solution(self, args, output):
        response = self.solution.singleNumber(*args)
        self.assertEqual(response, output, "expected: {} \n actual: {}\n".format(output, response))
