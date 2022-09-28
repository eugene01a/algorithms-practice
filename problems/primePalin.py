from unittest import TestCase

import ddt


class Solution(object):
    def palindromes(self, ndigits):
        if ndigits == 1:
            for i in range(10):
                yield i

        start = '1' + '0' * (ndigits // 2)
        end = '9' * (ndigits // 2)

        if ndigits % 2:  # odd
            for m in range(10):
                for n in range(int(start), int(end) + 1):
                    yield int(str(n) + str(m) + str(n[::-1]))
        else:  # even
            for n in range(int(start), int(end) + 1):
                yield int(str(n) + str(n[::-1]))

    def isPrime(self, x):
        if x == 1:
            return False
        if x == 2:
            return True
        for y in range(2, int(x ** 0.5 + 1)):
            if y % 2 == 0:
                return False
        return True

    def primePalindrome(self, N):
        length = len(str(N))
        while True:
            for x in self.palindromes(length):
                if x >= N and self.isPrime(x):
                    return x
            length += 1


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([6], 7),
        ([8], 11),
        ([1215122], 11),
    )
    def test_solution(self, args, output):
        response = self.solution.primePalindrome(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
