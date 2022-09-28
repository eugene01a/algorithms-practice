from unittest import TestCase

import ddt

'''
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
'''


class Solution(object):

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        if len(word1) > len(word2):
            queue_sm = [(word2, 0)]
            queue_lg = [(word1, 0)]
        else:
            queue_sm = [(word1, 0)]
            queue_lg = [(word2, 0)]
        visited_lg = set()
        visited_sm = set()
        word_sm, step_sm = queue_sm[-1]

        while queue_lg:
            word_lg, step_lg = queue_lg.pop(0)
            if len(word_lg) > len(word_sm):
                for i in range(len(word_lg)):
                    queue_lg.append((word_lg[:i] + word_lg[i + 1:], step_lg + 1))
            else:
                while len(word_sm) == len(word_lg):
                    print word_sm, word_lg
                    if word_lg == word_sm:
                        return step_lg + step_sm
                    else:
                        for i in range(len(word_lg)):
                            new_lg = word_lg[:i] + word_lg[i + 1:]
                            if new_lg not in visited_lg:
                                visited_lg.add(new_lg)
                                queue_lg.append((new_lg, step_lg + 1))
                            new_sm = word_sm[:i] + word_sm[i + 1:]
                            if new_sm not in visited_sm:
                                visited_sm.add(new_sm)
                                queue_sm.append((new_sm, step_sm + 1))
                        word_sm, step_sm = queue_sm.pop(0)


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([8], 2), ([9], 1), ([12], 3), ([18], 2), ([22], 3), ([13], 2), ([30], 3), ([27], 3), ([20], 2), ([21], 3),
        ([24], 3), ([12], 3))
    def test_solution(self, args, output):
        response = self.solution.numSquares(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
