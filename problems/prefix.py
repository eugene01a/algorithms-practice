import ddt
from unittest import TestCase


'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

All given inputs are in lowercase letters a-z.

'''

@ddt.ddt
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not len(strs):
            return ""
        sol = ""
        for i in range(len(min(strs))):
            c = strs[0][i]
            if all([s[i] == c for s in strs[1:]]):
                sol += c
            else:
                break
        return sol


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([["dog", "racecar", "car"]], ""),
        ([["flower", "flow", "flight"]], "fl")
    )
    def test_solution(self, args, output):
        response = self.solution.longestCommonPrefix(*args)
        assert response == output



