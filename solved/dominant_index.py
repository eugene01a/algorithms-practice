from unittest import TestCase

import ddt

'''
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
 

Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
 

Note:

nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].
'''


@ddt.ddt
class Solution(object):
    def dominantIndex(self, nums):
        ordered_nums = sorted(nums)
        max_num=ordered_nums[-1]
        if max_num >= ordered_nums[-2]*2:
            return nums.index(max_num)

        else:
            return -1

@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[3, 6, 1, 0]], 1),
        ([[1, 2, 3, 4]], -1),
        ([[1, 2, 3, 4]], -1),
        ([[49]*50], -1),
        ([[1]], 0)
    )
    def test_solution(self, args, output):
        response = self.solution.dominantIndex(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
