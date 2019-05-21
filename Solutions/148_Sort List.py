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


        # cut down the first part
        prev.next = None #截断

        l = self.sortList(head) #递归
        r = self.sortList(slow)
        return self.merge(l, r)


    #这是一种类似于创建一个头的DummyNode，把Head设置成Prev，Cur设置成head.next
    def merge(self, l, r):
        guard = cur = ListNode(0)
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
'''
# 思路
第一步，如何等分地划分，可以使用快慢指针的方式，当快指针到达结尾，那么慢指针到了中间位置，把链表进行截断分成了两个。

第二步，合并有序的序列，对于单链表来说，正好用到了Merge Two Sorted Lists里的把两个链表合并的方法。

'''