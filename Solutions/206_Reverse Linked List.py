'''
206. Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/
similar problem: "24. Swap Nodes in Pairs"
https://leetcode.com/problems/swap-nodes-in-pairs/discuss/171788/Python-or-Dummynode-tm

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively.
Could you implement both?
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode, tail=None) -> ListNode:
        '''
        recursion
        :param head: ListNode
        :return: ListNode
        '''
        if head: head.next, tail, head = tail, head, head.next
        return self.reverseList(head, tail) if head else tail

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        loop
        :param head: ListNode
        :return: ListNode
        '''
        # create tail, tail.next = None
        # start from node.val = 1
        # tail.next, head.next, head = head, tail.next, head.next
        # tail -> 1 -> Null
        tail = ListNode(0)
        # or None or 无论什么情况都存在的一个值： ListNode(float(-inf)
        while head: tail.next, head.next, head = head, tail.next, head.next
        return tail.next
# reverse order:
# tail = None
# --loop--
# tail = head
# head.next = tail
# head = head.next