'''

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def num2node(num):

            str_digits = list(str(num))
            node = None
            for str_digit in str_digits:
                prev_node = ListNode(str_digit)
                prev_node.next = node
                node = prev_node

            return node

        def list2number(ll):
            values = []

            node = ll
            # collect all values in ll
            while node.next:
                values.append(node.val)
                node = node.next

            values.append(node.val)

            # join and reverse, convert to int
            str_digits = [str(digit) for digit in values]
            str_number = ''.join(str_digits)[::-1]
            return int(str_number)

        # get first number from l1
        n1 = list2number(l1)
        # get second number from l2
        n2 = list2number(l2)
        # add numbers
        sum = n1 + n2

        return num2node(sum)


l1 = ListNode(1)
l1.next = ListNode(8)

l2 = ListNode(0)

sol = Solution()
response = sol.addTwoNumbers(l1, l2)
print(response)
