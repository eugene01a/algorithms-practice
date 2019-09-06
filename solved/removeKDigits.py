from unittest import TestCase

import ddt

'''
PROBLEM
'''


class Solution(object):
    def removeKdigits(self, num, k):
        steps = 0
        stack1 = reversed(list(num))
        sol = ''
        while stack1:
            d=stack1.pop()
            if stack1 and int(stack1[-1]) < int(d) and steps < k:
                steps += 1
            elif d == '0' and not sol:
                continue
            elif not stack1 and steps < k:
                continue
            else:
                sol += d
        if not sol:
            return '0'
        if steps <k:
            #all digits equal or ascending
            return sol[(k-steps)-1:]

        return sol

@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        (["1432219", 3], "1219"),
        (["10200", 1], "200"),
        (["10", 2], "0"),
        (["1111111", 3], "1111"),
        )
    def test_solution(self, args, output):
        response = self.solution.removeKdigits(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
