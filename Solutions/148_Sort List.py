'''
148. Sort List

https://leetcode.com/problems/sort-list/
similar problem: "147. Insertion Sort List"
https://leetcode.com/problems/insertion-sort-list/

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4

Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        prev = None
        fast = slow = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        mid = slow
        # cut down the first part
        prev.next = None #截断

        l = self.sortList(head) #递归
        r = self.sortList(mid)
        return self.merge(l, r)


    #这是一种类似于创建一个头的DummyNode，把Head设置成Prev，Cur设置成head.next
    def merge(self, l, r):
        guard = cur = ListNode(None)
        while l and r:
            if l.val <= r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r # l and r at least one is None
        return guard.next