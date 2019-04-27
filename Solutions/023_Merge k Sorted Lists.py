'''
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

解题思路：
归并k个已经排好序的链表。使用堆这一数据结构，首先将每条链表的头节点进入堆中，
然后将最小的弹出，并将最小的节点这条链表的下一个节点入堆，依次类推，
最终形成的链表就是归并好的链表。

-------------------------------------------------
reference：
入门堆（heapq）
https://blog.csdn.net/u013206202/article/details/78968438

heapq.heapify(list)
注：将列表转换为堆

>> list = [1,2,3,5,1,5,8,9,6]
>> heapq.heapify(list)
>> list
[1, 1, 3, 5, 2, 5, 8, 9, 6]
-------------------------------------------------
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        '''

        :param lists: : List[ListNode]
        :return: ListNode
        '''
        import heapq
        head = ListNode(-1)
        move = head
        heap = []
        heapq.heapify(heap)
        [heapq.heappush(heap, (l.val, i)) for i, l in enumerate(lists) if l]
        while heap:
            curval = curindex = heapq.heappop(heap)
            curhead = lists[curindex]
            curnext = curhead.next
            move.next = curhead
            curhead.next = None
            move = curhead
            curhead = curnext

            if curhead:
                lists[curindex] = curhead
                heapq.heappush(heap, (curhead.val, curindex))

        return head.next




