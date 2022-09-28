from unittest import TestCase

import ddt

'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

from collections import deque


class Solution(object):
    def numSquares(self, n):
        """
        BST
        :type n: int
        :rtype: int
        """
        nums = [p ** 2 for p in range(1, int(n ** 0.5) + 1)]
        visited = set()
        queue = deque()
        queue.append(n)
        steps = 0
        while queue:
            for _ in range(len(queue)):
                m = queue.popleft()
                if m == 0:
                    return steps
                elif m not in visited:
                    visited.add(m)
                else:
                    continue
                for num in nums:
                    queue.append(m - num)
                print m, visited, queue
            steps += 1


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
