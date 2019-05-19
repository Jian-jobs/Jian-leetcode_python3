'''
142. Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/
similar problem: "141. Linked List Cycle"
https://leetcode.com/problems/linked-list-cycle/

Given a linked list, return the node where the cycle begins.
If there is no cycle, return null.

To represent a cycle in the given linked list,
we use an integer pos which represents the position (0-indexed)
in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.


Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head  # or fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                while slow != head:
                    slow = slow.next
                    head = head.next
                return slow

        return None
# or
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head  # or fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

            while slow != head:
                slow = slow.next
                head = head.next
            return slow # or head

        return None
'''
思路：

大致意思是当Fast和Slow重合的时候，他们离开起始Loop的距离
# 和Head离开Loop起始的距离是相等的
'''