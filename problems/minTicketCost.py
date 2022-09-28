from unittest import TestCase

import ddt


class Solution:

    def minTicketCost(self, days, costs):
        N = len(days)

        def dp(start):
            if start >= N:
                return 0
            end = start
            ans = float('inf')
            for duration, cost in zip([1, 7, 30], costs):
                while end < N and days[end] < days[start] + duration - 1:
                    end += 1
                    ans = min(ans, dp(end) + cost)
            return ans

        return dp(0)


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(([[1, 4, 6, 7, 8, 20], [7, 2, 15]], 6),
              ([[1, 4, 6, 7, 8, 20], [2, 7, 15]], 11)
              )
    def test_solution(self, args, output):
        response = self.solution.minTicketCost(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
