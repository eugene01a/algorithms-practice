from unittest import TestCase

import ddt

'''
'''


class Solution(object):

    def countAndSay(self, n):
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        sol = ''
        prev = self.countAndSay(n - 1)
        i = 0
        length = len(prev)
        while i < length:
            j = i
            count = 0
            while j < length and prev[j] == prev[i]:
                count += 1
                j += 1
            sol += (str(count) + prev[i])
            i = j
        return sol


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([4], '1211'),
        ([5], '111221'),
        ([2], '11'),
        ([1], '1'),
        ([3], '21'),
    )
    def test_solution(self, args, output):
        response = self.solution.countAndSay(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
