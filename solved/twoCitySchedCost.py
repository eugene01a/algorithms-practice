from collections import defaultdict
from unittest import TestCase

import ddt


class Solution:

    def twoCitySchedCost(self, costs):

        costs.sort(key = lambda x: x[0]-x[1])

        iSum=0
        for i in costs[:len(costs)//2]:
            iSum += i[0]

        jSum = 0
        for j in costs[len(costs)//2:]:
            jSum += j[1]

        return iSum + jSum


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        (["barfoothefoobarman", ["foo", "bar"]], [0, 9]),
        (["lingmindraboofooowingdingbarrwingmonkeypoundcake",
          ["fooo", "barr", "wing", "ding", "wing"]], [0, 9]),
        (["wordgoodgoodgoodbestword", ["word", "good", "best", "word"]], []),
        (["barfoofoobarthefoobarman", ["bar", "foo", "the"]], [6, 9, 12]),
        ([["wordgoodgoodgoodbestword", ["word", "good", "best", "good"]], [8]]))
    def test_solution(self, args, output):
        response = self.solution.findSubstring(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
