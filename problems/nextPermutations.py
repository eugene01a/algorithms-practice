from unittest import TestCase

import ddt


class Solution(object):
    def nextPermutation(self, nums):
        length=len(nums)
        for i in range(length-1, 0, -1):
            if nums[i] > nums[i-1]:
               for j in range(i,length):
                   if nums[j] < nums[i-1]:
                        nums[j-1], nums[i] = nums[i], nums[j-1]
                        return nums

        def reverse():
            i=0
            j=length-1
            while i != j:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1

        reverse()
        return nums


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[1, 1, 2]], [1,2,1]))
    def test_solution(self, args, output):
        response = self.solution.nextPermutation(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
