from unittest import TestCase

import ddt

'''
Implement strStr().

Return list of indexes of the first occurrences of needle in haystack.

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
        i = 0
        j = 0
        sol = []

        while j < len(needle) and i < len(haystack):
            print "i={}, j={}".format(i, j)
            print "haystack[i] == needle[0], {} == {}".format(haystack[i], needle[0])
            print  "needle[j] == haystack[i + j], {} == {}".format(needle[j], haystack[i + j])
            if haystack[i] == needle[0] and needle[j] == haystack[i + j]:


                if j == len(needle) - 1:
                    print "match!"
                    sol.append(i)
                    i = i + j + 1
                    j = 0
                else:

                    j += 1
            else:
                # i!=needle[0]
                i += 1
                j = 0

        return sol


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        (["helloll", 'll'], [2, 5])
    )
    def test_solution(self, args, output):
        response = self.solution.strStr(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
