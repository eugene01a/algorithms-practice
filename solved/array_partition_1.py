from unittest import TestCase

import ddt

'''
Array Partition I
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].


min(i,j) where j-i is small as possible


[1,4,3,2,100,50,20,5] -> [1,2,3,4,5,20,50,100]
min(1,2)+min(3,4)+min(5,20)+min(50,100)
1+3+5+50=59

sort nums
sum+=i, i+=2 while i<len(nums)/2



'''


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        sum = 0
        while i < len(nums):
            sum += nums[i]
            i += 2

        return sum


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[1,4,3,2]], 4),
    )
    def test_solution(self, args, output):
        response = self.solution.arrayPairSum(*args)
        self.assertEqual(response, output, "expected: {} \n actual: {}\n".format(output, response))
