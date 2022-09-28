from unittest import TestCase

import ddt

'''
'''

class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

class Solution(object):

    def reverseKGroup(self, head, k):
        cur = head
        while cur and cur.next and k > 0:
            cur, cur.next = cur.next, cur
            cur = cur.next.next
            k -= 1
            return head



@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        )
    def test_solution(self, args, output):
        response = self.solution.reverseKGroup(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
