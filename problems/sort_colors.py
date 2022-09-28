from unittest import TestCase

import ddt

'''
75. Sort Colors
Medium

1651

158

Favorite

Share
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
'''


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        : rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        end = len(nums) - 1
        j = end
        while i < end:
            if i == j:
                j = end
                i += 1
            elif nums[i] > nums[j]:
                old = nums[i]
                nums[i] = nums[j]
                nums[j] = old
                j -= 1
            else:
                j -= 1
        return nums


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[2, 0, 2, 1, 1, 0]], [0, 0, 1, 1, 2, 2]),
    )
    def test_solution(self, args, output):
        response = self.solution.sortColors(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
