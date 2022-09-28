from unittest import TestCase

import ddt


class Solution:
    def permuteUnique(self, nums):
        ans=[]
        nums.sort()
        visited=set()
        def DFS(perm, other_nums):
            if not other_nums:
                visited.add(''.join(perm))
                ans.append(perm)
                return
            for j in range(len(other_nums)):

                DFS(perm+[other_nums[j]], other_nums[:j] + other_nums[j + 1:])

        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            else:
                visited.add(nums[i])
                DFS([nums[i]], nums[:i]+nums[i+1:])
        return ans


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[1, 1, 2]], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]))
    def test_solution(self, args, output):
        response = self.solution.permuteUnique(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
