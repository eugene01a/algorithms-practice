from unittest import TestCase

import ddt


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def helper(nums, target, t):
            if not nums:
                return -1
            else:
                i = len(nums) // 2
                if target == nums[i]:
                    return i + t
                elif target > nums[i]:
                    nums=nums[i + 1:]
                    t=t+i+1

                else:
                    # target<nums[i]
                    nums = nums[:i]

                return helper(nums, target, t)


        return helper(nums, target, 0)
@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[-1, 0, 3, 5, 9, 12], 3], 2),
        ([[-1,0,3,5,9,12], 9], 4),
    )
    def test_solution(self, args, output):
        response = self.solution.search(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
