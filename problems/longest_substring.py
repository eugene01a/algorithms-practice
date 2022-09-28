import ddt
from unittest import TestCase

'''
DETAILS
'''


@ddt.ddt
class Solution(object):
    def _longest_substring(self, s):
        clist = list(s)
        current = []
        lengths = []
        for ch in clist:
            if ch in current:
                # ch is repeated, start of new substring
                lengths.append(len(current))
                current = []
            current.append(ch)
        return max(lengths)

    def lengthOfLongestSubstring(self, s):
        l = res = 0
        memo = {}
        for r,x in enumerate(s):
            print("r={}, x={}".format(r,x))
            if x in memo:         # when we meet repeating characters( substring does not meet requirement, update left pointer)
                l = max(l, memo[x] + 1)    # why don't we use "l = memo[x] + 1"? refer to testcase like 'abba'
            print('adding memo[{}]={}'.format(x,r))
            memo[x] = r  # update new index for character x (memo[x] will always be the largest index in the characters we visited)
            res = max(res, r - l + 1)      # inclusive, l: first index of the string, r: last index of the string
        return res

@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        (["abcabcbb"], 3),
        (["pwwkew"], 3),
        (["bbbbb"], 1),
    )
    def test_solution(self, args, output):
        response = self.solution.longest_substring(*args)
        assert response == output



