from unittest import TestCase

import ddt

'''
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
'''


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        def convert_nums(nums):
            for i in range(len(nums)):
                if type(nums[i]) == str:
                    nums[i] = int(nums[i])
            return nums

        def add(m):
            sol = 0
            for char in m:
                sol += int(char)
            return sol

        def flip(n):
            n=str(n)
            if n[0] == '-':
                return n[1:]
            else:
                return '-' + n

        sol = 0
        visited = []
        nums = nums
        stack = [nums]
        size = len(nums)
        while stack:
            n = stack.pop()
            for i in range(size):
                m = list(n)
                m[i] = flip(m[i])
                if m in visited:
                    continue
                if add(m) == S:
                    sol += 1
                    print m
                stack.append(m)
                visited.append(m)
        return sol


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[1, 1, 1, 1, 1], 3], 5),
        ([[1, 0], 1], 2),
    )
    def test_solution(self, args, output):
        response = self.solution.findTargetSumWays(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
