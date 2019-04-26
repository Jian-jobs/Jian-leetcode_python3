'''
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# iteration


class Solution:
    def mergeTwoLists(self, l1, l2) -> ListNode:
        '''

        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode,
        '''

        dummy = ListNode(0)
        head = dummy
        if not l2:
            return l1
        if not l1:
            return l2
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 if l1 else l2
        return dummy.next

# recursion

class Solution:
    def mergeTwoLists(self, l1, l2) -> ListNode:
        '''

        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode,
        '''
        dummy = ListNode(0)
        head = dummy
        if not l1 and not l2:
            return None
        elif not l2:
            return l1
        elif not l1:
            return l2
        if l1.val <= l2.val:
            head= l1
            head.next = self.mergeTwoLists(l1.next, l2)
        else:
            head= l2
            head.next = self.mergeTwoLists(l1, l2.next)
        return head

