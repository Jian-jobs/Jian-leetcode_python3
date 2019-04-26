'''
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        '''

        :param head: ListNode
        :return: ListNode
        '''
        dummy = ListNode(0)
        dummy.next = head
        res = dummy

        while res.next and res.next.next:
            first = res.next
            second = res.next.next
            res.next = second
            first.next = second.next
            second.next = first
            res = res.next.next

        return dummy.next

