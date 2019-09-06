'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''

from collections import defaultdict
from unittest import TestCase

import ddt
from nose.plugins.attrib import attr


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if len(t) is 0 or len(s) is 0:
            return ""

        tChars = defaultdict(int)
        for c in t:
            tChars[c] += 1

        res = None

        start = 0
        missing = len(t)

        for end in range(len(s)):
            if s[end] in tChars:
                if tChars[s[end]] > 0:
                    missing -= 1
                tChars[s[end]] -= 1

            if missing is 0:
                while missing is 0:
                    if s[start] in tChars:
                        if tChars[s[start]] >= 0:
                            missing += 1
                        tChars[s[start]] += 1
                    start += 1
                if res is None or end - start + 2 < res[1] - res[0]:
                    res = (start - 1, end + 1)

        return s[res[0]: res[1]] if res is not None else ""


@ddt.ddt
@attr("memoization")
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        (["ADOBECODEBANC", "ABC"],'BANC'),
    )
    def test_solution(self, args, output):
        response = self.solution.minWindow(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
