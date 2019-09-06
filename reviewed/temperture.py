from unittest import TestCase
from nose.plugins.attrib import attr
import ddt

class Solution(object):
    def dailyTemperatures(self, T):
        length=len(T)
        sol=[0]*length
        stack=[]
        for i in range(length-1, -1, -1):
            while stack and T[stack[-1]]<T[i]:
                 stack.pop()
            if stack:
                sol[i]=stack[-1] - i
            stack.append(i)
        print sol
        return sol

@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[73, 74, 75, 71, 69, 72, 76, 73]],
              [1, 1, 4, 2, 1, 1, 0, 0]),
    )
    @attr("stack")
    def test_solution(self, args, output):
        response = self.solution.dailyTemperatures(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
