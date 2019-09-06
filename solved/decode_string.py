from unittest import TestCase

import ddt

'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
 '''


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        sol = ''
        brackets = []
        stack = []
        digits = [str(n) for n in range(1, 10, 1)]
        for i in range(len(s)):
            if s[i] == "]":
                substring = ''
                while stack[-1] != "[":
                    substring = substring + stack.pop()
                stack.pop()  # pop bracket
                n = int(stack.pop())
                substring *= n
                stack.append(substring)
            else:
                stack.append(s[i])

        return ''.join(stack)


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        (['3[a]2[bc]'], 'aaabcbc'),
        (['3[a2[c]]'], 'accaccacc'),
        (['2[abc]3[cd]ef'], 'abcabccdcdcdef'),
    )
    def test_solution(self, args, output):
        response = self.solution.decodeString(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
