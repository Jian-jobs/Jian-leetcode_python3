'''
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in reverse order and each of their nodes contain a single digit.

Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def my_test(self):
        print(self.val)
        if self.next:
            self.next.my_test()


class Solution:
    def addTwoNumbers(self, l1, l2):
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0
        def tolist(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = tolist(n / 10)
            return node
        return tolist(toint(l1) + toint(l2))


l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)
ls = Solution().addTwoNumbers(ListNode(l2),ListNode(l2))
print(ls)
