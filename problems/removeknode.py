from unittest import TestCase

import ddt

'''
PROBLEM
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def list2link(l):
    if list == []:
        return None
    node = ListNode(l[0])
    n = node
    for i in range(1, len(l)):
        n.next = ListNode(l[i])
        n = n.next
    return node


def link2list(node):
    if node is None:
        return []
    n = node
    l = [node.val]
    while n.next:
        l.append(n.next.val)
        n = n.next
    return l


from collections import defaultdict

class Solution(object):
    def removeNthFromEnd(self, head, n):
        head = list2link(head)

        if head is None:
            return link2list(None)
        map = defaultdict(lambda: None)
        node = head
        ct = 1
        while node:
            map[ct] = node
            node = node.next
            ct += 1

        if map[ct - n - 1]:
            map[ct - n - 1].next = map[ct - n + 1]
        else:
            head=map[ct - n + 1]

        return link2list(head)


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([[1, 2, 3, 4, 5], 2], [1, 2, 3, 5]),
        ([[1, 2, 3, 4, 5], 1], [1, 2, 3, 4]),
        ([[1], 1], []),
        ([list()], []),
        ([[1,2], 2], [2]),
        ([[1,2,3], 3], [2,3]),
    )
    def test_solution(self, args, output):
        response = self.solution.removeNthFromEnd(*args)
        self.assertEqual(response, output, "\n\nexpected: {} \n actual: {}\n".format(output, response))
