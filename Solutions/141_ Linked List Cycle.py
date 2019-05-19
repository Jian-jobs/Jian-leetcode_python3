'''
141. Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/
similar problem: "142. Linked List Cycle II"
https://leetcode.com/problems/linked-list-cycle-ii/

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer
pos which represents the position (0-indexed) in the linked list
where tail connects to. If pos is -1, then there is no cycle in the
linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list,
where tail connects to the second node.

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head # or fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True

        return False
'''
思路：
基于上面的想法，Floyd用两个指针，一个慢指针（龟）每次前进一步，
快指针（兔）指针每次前进两步（两步或多步效果时等价的，只要一个比另一个快就行）。
如果两者在链表头以外的某一点相遇（即相等）了，那么说明链表有环，
否则，如果（快指针）到达了链表的结尾，那么说明没环。

'is' and '==':
当变量是数字、字符串、元组，列表，字典时，is和==都不相同， 不能互换使用！
当比较值时，要使用==，比较是否是同一个内存地址时应该使用is。

'''

