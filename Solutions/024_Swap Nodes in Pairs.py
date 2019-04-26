'''
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

reference: https://leetcode.com/problems/swap-nodes-in-pairs/discuss/171788/Python-or-Dummynode-tm

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# iteration


class Solution:
    def swapPairs(self, head):
        '''

        :param head: ListNode
        :return: ListNode
        '''
        dummy = ListNode(0)
        dummy.next = head
        res = dummy
        if not head or not head.next: return head
        while res.next and res.next.next:
            first = res.next
            second = res.next.next
            res.next = second
            first.next = second.next
            second.next = first
            res = res.next.next

        return dummy.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

l = Solution().swapPairs(l1)

print(l1.val)

# recursion


class Solution:
    def swapPairs(self, head):
        '''

        :param head: ListNode
        :return: ListNode
        '''
        if not head or not head.next: return head
        new_start = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(new_start)
        return head

