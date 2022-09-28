from unittest import TestCase

import ddt

'''
Contains Duplicate
  Go to Discuss
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        un=set(nums)
        if len(un) == len(nums):
            return False
        else:
            return True



@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[1, 2, 3, 1]], True),
        ([[1, 2, 3, 4]], False),
        ([[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]], True),

    )
    def test_solution(self, args, output):
        response = self.solution.containsDuplicate(*args)
        self.assertEqual(response, output, "expected: {} \n actual: {}\n".format(output, response))
