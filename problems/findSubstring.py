from collections import defaultdict
from unittest import TestCase

import ddt


class Solution(object):
    def findSubstring(self, s, words):
        if not words or not s:
            return []
        sols, length, n = [], len(words[0]), len(words)
        hmap, stack = defaultdict(list), list(words)

        def reset():
            while stack:
                word = stack.pop()
                hmap[word[0]].append(word[1:])

        reset()
        i, j = 0, 0
        while i < len(s) - 1:
            if len(stack) == n:
                sols.append(j)
                j += length
                word = stack.pop(0)
                hmap[word[0]].append(word[1:])

            key = s[i]
            value = s[i + 1:i + length]

            if key in hmap:
                if value in hmap[key]:
                    stack.append(key + value)
                    hmap[key].remove(value)
                    i += length

                else:
                    if stack and key + value == stack[-1]:
                        reset()
                        stack.append(key + value)
                        hmap[key].remove(value)
                        j = i
                        i += length
                    else:
                        i += 1
                        j = i
            else:
                reset()
                i += 1
                j = i

        return sols


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        (["barfoothefoobarman", ["foo", "bar"]], [0, 9]),
        (["lingmindraboofooowingdingbarrwingmonkeypoundcake",
          ["fooo", "barr", "wing", "ding", "wing"]], [0, 9]),
        (["wordgoodgoodgoodbestword", ["word", "good", "best", "word"]], []),
        (["barfoofoobarthefoobarman", ["bar", "foo", "the"]], [6, 9, 12]),
        ([["wordgoodgoodgoodbestword", ["word", "good", "best", "good"]], [8]]))
    def test_solution(self, args, output):
        response = self.solution.findSubstring(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))


