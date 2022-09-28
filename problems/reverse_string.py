from unittest import TestCase

import ddt

'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

'''


@ddt.ddt
class Solution(object):
    def reverseString(self, s):
        '''
        hello
        elloh move char at idx to -idx
        lloeh
        loleh
        olleh

        '''

        def helper(idx):
            if idx < len(s) / 2:
                idx2 = len(s) - idx - 1
                second_char = s[idx2]
                first_char = s[idx]
                s[idx2] = first_char
                s[idx] = second_char
                helper(idx + 1)
            else:
                return None

        helper(0)
        return s


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([["h", "e", "l", "l", "o"]], ["o", "l", "l", "e", "h"]),
        ([["H", "a", "n", "n", "a", "h"]], ["h", "a", "n", "n", "a", "H"]),
    )
    def test_solution(self, args, output):
        response = self.solution.reverseString(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
