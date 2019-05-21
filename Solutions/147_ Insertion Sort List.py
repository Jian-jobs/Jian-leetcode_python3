'''
147. Insertion Sort List

https://leetcode.com/problems/insertion-sort-list/
similar problem: "148. Sort List"
https://leetcode.com/problems/sort-list/

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# my answer:
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        # if not head or not head.next: return head

        dummy = ListNode(0)
        dummy.next = head

        while head and head.next:
            if head.val > head.next.val: #找前一个数比后一个数大，否则继续
                node = head.next # node： 需要insert 的数字
                pos = dummy # pos： the position where node is gonna insert after
                while pos.next.val < node.val:
                    pos = pos.next
                head.next = node.next # 以下三行： 把 node insert在 pos和pos.next之间
                node.next = pos.next
                pos.next = node

            else:
                head = head.next
        return dummy.next



# understandable solution:
class Solution:
    def insertionSortList(self, head):

        dummyHead = ListNode(0)
        dummyHead.next = nodeToInsert = head

        while head and head.next:
            if head.val > head.next.val:
                # Locate nodeToInsert.
                nodeToInsert = head.next
                # Locate nodeToInsertPre.
                nodeToInsertPre = dummyHead
                while nodeToInsertPre.next.val < nodeToInsert.val:
                    nodeToInsertPre = nodeToInsertPre.next

                head.next = nodeToInsert.next
                # Insert nodeToInsert between nodeToInsertPre and nodeToInsertPre.next.
                nodeToInsert.next = nodeToInsertPre.next
                nodeToInsertPre.next = nodeToInsert
            else:
                head = head.next

        return dummyHead.next



#other solution:
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        ## we need three pointer here, p is the position where cur is gonna inser after
        ## cur is the element we need to compare each time
        ## dummy is to return the sorted list, and in case head is changed
        p = dummy = ListNode(0)
        cur = dummy.next = head

        ## traverse to the last second node
        while cur and cur.next:
            ## compare cur node with next node val
            ## if the sequence is sorted already, keep looking ahead
            ## continue is a must here for the next iteration
            next_val = cur.next.val
            if cur.val <= next_val:
                cur = cur.next
                continue

            ## if there is an element which is smaller than previous sequence
            ## we need to find a proper position to insert this small element
            if p.next.val > next_val:
                p = dummy.next

            ## p stops at the element which is smaller than next_val
            ## eg 1,2,5,6,7,4, 8,9 --> since 4 is bigger than 1, 2
            ## we use p.next.val to compare, hence p would point element 2
            ## update: cur would point at 7
            while p.next.val <= next_val:
                p = p.next

            ## exchange, insertion
            ## for the above example, p.next should be cur.next which is 4
            ## cur.next.next should concatenate the elements in the sorted sequence, in this case 5,6,7
            ## cur.next should be cur.next.next which is 8
            ## update: basically it's an operation to find the proper position of the cur.next.val and reconstruct the list
            ## update2: if we break the syntax down, it becomes:
            ## new = cur.next
            ## cur.next = new.next
            ## new.next = p.next
            ## p.next = new

            p.next, cur.next.next, cur.next = cur.next, p.next, cur.next.next

        return dummy.next





