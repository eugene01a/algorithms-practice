from unittest import TestCase

import ddt

'''
PROBLEM
'''


class Solution(object):
    def minDistance(self, word1, word2):
        memo={}

        def dp(i, j):
            if (i,j) in memo:
                return memo[i,j]
            if len(word1) == i or len(word2) == j:
                ans= len(word1) + len(word2) - i - j
            elif word1[i] == word2[j]:
                ans= dp(i + 1, j + 1)
            else:
                ans= 1 + min(dp(i + 1, j), dp(i, j + 1))
            memo[i,j]=ans
            return ans
        return dp(0, 0)


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        (["eat", "sea"], 2),
    )
    def test_solution(self, args, output):
        response = self.solution.minDistance(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
