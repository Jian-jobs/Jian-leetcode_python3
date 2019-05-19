'''
21. Merge Two Sorted Lists

https://leetcode.com/problems/two-sum/
similar problem: "23. Merge k Sorted Lists"
https://leetcode.com/problems/merge-k-sorted-lists/

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


# my answer:
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        res = dummy
        if l1 is None: return l2
        if l2 is None: return l1
        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1 #不是l1.val!!
                l1 = l1.next
            else:
                res.next = l2 #不是l2.val!!
                l2 = l2.next
            res = res.next
        res.next = l1 if l1 else l2 #没有这行的话最后一个数不显示
        return dummy.next


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
        if not l1 and not l2: # better condition setting
            return None
        elif not l2:
            return l1
        elif not l1:
            return l2
        if l1.val <= l2.val:
            head= l1
            head.next = self.mergeTwoLists(l1.next, l2) #self.function(element1, element2)
        else:
            head= l2
            head.next = self.mergeTwoLists(l1, l2.next)
        return head