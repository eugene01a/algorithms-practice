from unittest import TestCase

import ddt


class Solution:
    def getPermutation(self, n, k):
        nums = [str(i) for i in range(1, n+1)]
        print("nums={}".format(nums))
        fact = [1] * n
        for i in range(1,n):
            fact[i] = i*fact[i-1]
        k -= 1
        ans = []
        for i in range(n, 0, -1):
            id = k / fact[i-1]
            k %= fact[i-1]
            ans.append(nums[id])
            nums.pop(id)
        return ''.join(ans)


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([3,3], "213"),
        ([4,9], "2314"),
    )
    def test_solution(self, args, output):
        response = self.solution.getPermutation(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
