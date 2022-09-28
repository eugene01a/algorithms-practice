from unittest import TestCase

import ddt

'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
        
'''


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if needle not in haystack:
            return -1

        i = 0
        j = 0
        sol = -1

        while j < len(needle):
            if haystack[i] == needle[0] and needle[j] == haystack[i + j]:
                j += 1
            else:
                # i!=needle[0]
                i += 1
                j = 0
        return i


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        (["hello", 'll'], 2),
        (["aaaaa", 'bba'], -1),
    )
    def test_solution(self, args, output):
        response = self.solution.strStr(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
