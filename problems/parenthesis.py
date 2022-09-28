from unittest import TestCase

import ddt

'''
DETAILS

Keep track of counts of open and close brackets.

Initialize these counts as 0.
Recursively call the _printParenthesis() function until open bracket count is less than the given n.
If open bracket count becomes more than the close bracket count, then put a closing bracket and recursively call for the remaining brackets.
If open bracket count is less than n, then put an opening bracket and call _printParenthesis() for the remaining brackets.


Recursion is the key here.
Divide the N into N/2 and N/2 (Count for open and closed parentheses ).
Select the open parentheses, add it to the result string and reduce its count and make a recursive call.
Select the close parentheses, add it to the result string and reduce its count and make a recursive call.
To print only valid parentheses, make sure at any given point of time, close parentheses count is not less that open parentheses count because it means close parentheses has been printed with its respective open parentheses.

'''


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        op = n
        cp = n
        sol = []

        def helper(op, cp, s):
            if op == 0 and cp == 0:
                sol.append(s)
            if op > cp:
                return
            if op > 0:
                helper(op - 1, cp, s + '(')
            if cp > 0:
                helper(op, cp - 1, s + ')')

        helper(op, cp, "")
        return set(sol)


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([3], set(['((()))', '()()()', '()(())', '(())()', '(()())'])),
    )
    def test_solution(self, args, output):
        response = self.solution.generateParenthesis(*args)
        self.assertEqual(response, output, "expected: {} \n actual: {}\n".format(output, response))
