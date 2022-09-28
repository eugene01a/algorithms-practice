from itertools import product
from unittest import TestCase

import ddt

'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
'''


class Solution:
    '''
    dp[n] means the substring s[:n] if match the pattern i
    dp[0] means the empty string '' or s[:0] which only match the pattern '*'
    use the reversed builtin because for every dp[n+1] we use the previous 'dp'
    '''

    def isMatch(self, s, p):
        print s, p
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False] * length
        print dp
        for i in p:
            if i != '*':
                for n in reversed(range(length)):
                    dp[n + 1] = dp[n] and (i == s[n] or i == '?')
                    print dp
            else:
                for n in range(1, length + 1):
                    dp[n] = dp[n - 1] or dp[n]
                    print dp
            dp[0] = dp[0] and i == '*'
            print dp
        return dp[-1]


class Attempt:

    def isMatch(self, s, p):
        if (not p and not s) or (not s and p[0] == "*"):
            return True
        elif (not p and s) or (not s and p):
            return False
        elif s[0] == p[0] or p[0] == "?":
            p = p[1:]
            s = s[1:]
        elif p[0] == "*":
            p = p[1:]
            while s:
                if p and p[0] == s[0]:
                    break
                else:
                    s = s[1:]
        else:
            return False
        return self.isMatch(s, p)


@ddt.ddt
class LeetCodeTest(TestCase):

    @ddt.unpack
    @ddt.data(*product(
        [
            Attempt(),
            Solution()
        ],
        [
            (["aa", "a"], False),
            (["aa", "*"], True),
            (["cb", "?a"], False),
            (["adceb", "*a*b"], True),
            (["acdcb", "a*c?b"], False)
        ]
    ))
    def test_solution(self, fn, (args, output)):
        response = fn.isMatch(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
